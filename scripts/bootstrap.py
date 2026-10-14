"""Title: Prepare the Google Cloud CLI locally.
Description: Find an installed SDK or download a hash-verified portable archive.
References: https://docs.cloud.google.com/sdk/docs/downloads-versioned-archives
https://docs.cloud.google.com/sdk/gcloud/reference/topic/startup
No cloud resources, IAM policies, APIs or billing settings are changed here.
"""
import hashlib, os, pathlib, platform, shutil, subprocess, sys, tarfile, tempfile, urllib.request, zipfile

VERSION = '589.0.0'
ARCHIVES = {
 ('Windows','x86_64'): ('google-cloud-sdk-589.0.0-windows-x86_64-bundled-python.zip','b9c2f4f296154f55e8a31a6979106573bc1ad8691041d4a32ea90c1834fdf995'),
 ('Linux','x86_64'): ('google-cloud-cli-589.0.0-linux-x86_64.tar.gz','817026aec0adea0e2ee8ed3a1ba3eabfe9e5177581fbe16595a8fe495a601300'),
 ('Linux','arm64'): ('google-cloud-cli-589.0.0-linux-arm.tar.gz','c7b9abef0649e0fccc70bf2aaaa031a0aa6202863e45fabe938698dc93d4934c'),
 ('Darwin','x86_64'): ('google-cloud-cli-589.0.0-darwin-x86_64.tar.gz','b49e8cb9d348267d46fade7b9c916a1aed7ce0ec07e142ce41cc0d24a95a9651'),
 ('Darwin','arm64'): ('google-cloud-cli-589.0.0-darwin-arm.tar.gz','71b37ca07ab0f9bc43898e42c913e10f143166230ab31e0bbea3632dbc77b010')
}
LOCAL = pathlib.Path.home()/'.gcp-audit'

def inside(child, parent):
    return child.resolve().is_relative_to(parent.resolve())

def extract_archive(archive, destination):
    destination = pathlib.Path(destination)
    if zipfile.is_zipfile(archive):
        with zipfile.ZipFile(archive) as z:
            for member in z.infolist():
                if not inside(destination/member.filename, destination) or (member.external_attr >> 16) & 0o170000 == 0o120000:
                    raise ValueError('Unsafe archive member')
            z.extractall(destination)
    else:
        with tarfile.open(archive) as t:
            t.extractall(destination, filter='data')

def sdk_root():
    candidates = [LOCAL/'sdk'/VERSION/'google-cloud-sdk']
    for name in ['gcloud', 'gcloud.cmd', 'gcloud.ps1']:
        found = shutil.which(name)
        if found:
            candidates.append(pathlib.Path(found).resolve().parent.parent)
    if os.name == 'nt':
        candidates.append(pathlib.Path(os.environ.get('LOCALAPPDATA',''))/'Google/Cloud SDK/google-cloud-sdk')
    return next((x for x in candidates if (x/'lib/gcloud.py').is_file()),None)

def ensure_sdk():
    if not (3,12) <= sys.version_info[:2] <= (3,15):
        raise RuntimeError('Python 3.12–3.15 is required; use Bootstrap.ps1 on Windows or a supported Python installation.')
    existing = sdk_root()
    if existing:
        return existing
    arch = {'AMD64':'x86_64','aarch64':'arm64','arm64':'arm64','x86_64':'x86_64'}.get(platform.machine())
    item = ARCHIVES.get((platform.system(),arch))
    if not item:
        raise RuntimeError('Unsupported bootstrap platform; install the official Google Cloud CLI before collection.')
    filename, expected = item
    destination = LOCAL/'sdk'/VERSION
    if destination.exists():
        raise RuntimeError(f'Incomplete installation exists at {destination}; inspect it before retrying. It will not be overwritten.')
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='gcp-audit-sdk-') as temp:
        archive = pathlib.Path(temp)/filename
        url = 'https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/'+filename
        print(f'Installing portable Google Cloud CLI {VERSION} from Google into {destination}', file=sys.stderr)
        with urllib.request.urlopen(url,timeout=90) as response, archive.open('wb') as out:
            shutil.copyfileobj(response,out)
        with archive.open('rb') as stream:
            actual=hashlib.file_digest(stream,'sha256').hexdigest()
        if actual != expected:
            raise RuntimeError('SDK checksum mismatch; installation stopped before extraction or execution.')
        extract_archive(archive,pathlib.Path(temp)/'unpacked')
        root=pathlib.Path(temp)/'unpacked/google-cloud-sdk'
        if not (root/'lib/gcloud.py').is_file():
            raise RuntimeError('Archive lacks the expected SDK launcher')
        # Publish only a fully verified extraction. No PATH/profile changes.
        shutil.copytree(root,destination/'google-cloud-sdk')
    return destination/'google-cloud-sdk'

def launcher(root):
    # Execute Python directly so Windows .cmd cannot interpret shell metacharacters.
    return [sys.executable,str(pathlib.Path(root)/'lib/gcloud.py')]

def environment(account):
    env = {k:v for k,v in os.environ.items() if not k.upper().startswith('CLOUDSDK_') and k not in {'GOOGLE_APPLICATION_CREDENTIALS','GOOGLE_CLOUD_PROJECT'}}
    config=LOCAL/'accounts'/hashlib.sha256(account.encode()).hexdigest()[:20]
    config.mkdir(parents=True,exist_ok=True)
    env.update(CLOUDSDK_CONFIG=str(config), CLOUDSDK_CORE_DISABLE_PROMPTS='1',
        CLOUDSDK_CORE_SHOULD_PROMPT_TO_ENABLE_API='false',
        CLOUDSDK_COMPONENT_MANAGER_DISABLE_UPDATE_CHECK='1',
        CLOUDSDK_CORE_ACCOUNT=account, CLOUDSDK_CORE_LOG_HTTP='false',
        CLOUDSDK_CORE_VERBOSITY='warning', CLOUDSDK_CORE_UNIVERSE_DOMAIN='googleapis.com',
        CLOUDSDK_PYTHON=sys.executable, CLOUDSDK_PAGER='', PAGER='')
    return env

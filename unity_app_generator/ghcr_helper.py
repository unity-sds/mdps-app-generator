import os
import base64

import logging

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app_pack_generator import DockerUtil

logger = logging.getLogger(__name__)

class GHCRHelper(object):

    def __init__(self, docker_util : 'DockerUtil'):

        self.docker_util = docker_util

    def docker_login(self, username=None, token=None, registry = "ghcr.io"):

        username = username or os.environ.get("GHCR_USERNAME", None)
        token = token or os.environ.get("GHCR_TOKEN", None)

        if username is None:
            raise Exception(f"Github Container Registry username not defined either through argument ot GHCR_USERNAME environment variable")
    
        if token is None:
            raise Exception(f"Github Container Registry token not defined either through argument ot GHCR_TOKEN environment variable")
        
        logger.info(f"Logging into Docker using GHCR credentials for user: {username}")
        
        response = self.docker_util.docker_client.login(
            username=username,
            password=token,
            registry=registry,
        )

        return registry
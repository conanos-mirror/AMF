from conans import ConanFile, CMake, tools
from conanos.build import config_scheme
import os, shutil

class AmfConan(ConanFile):
    name = "AMF"
    version = "1.4.9"
    description = "The Advanced Media Framework (AMF) SDK provides developers with optimal access to AMD devices for multimedia processing"
    url = "https://github.com/conanos/AMF"
    homepage = "https://github.com/GPUOpen-LibrariesAndSDKs/AMF"
    license = "MIT"
    generators = "visual_studio", "gcc"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = { 'shared': True, 'fPIC': True }

    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        del self.settings.compiler.libcxx

        config_scheme(self)

    def source(self):
        url_ = 'https://github.com/GPUOpen-LibrariesAndSDKs/AMF/archive/v{version}.tar.gz'
        tools.get(url_.format(version=self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def build(self):
        pass

    def package(self):
        self.copy("*", dst=os.path.join(self.package_folder,"include","AMF"),
                  src=os.path.join(self.build_folder,self._source_subfolder,"amf","public","include"))

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)


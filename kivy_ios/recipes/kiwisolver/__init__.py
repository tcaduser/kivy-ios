from kivy_ios.toolchain import CythonRecipe, shprint
from os.path import join
import sh
import shutil


class KiwiSolverRecipe(CythonRecipe):
    site_packages_name = 'kiwisolver'
    version = '1.3.2'
    url = 'https://github.com/nucleic/kiwi/archive/{version}.zip'
    depends = ["python"]
    hostpython_prerequisites = ["cppy",]
    cythonize = False
    library = "libkiwisolver.a"

    def get_recipe_env(self, arch=None, with_flags_in_cc=True):
        env = super().get_recipe_env(arch)

        env['CXX_ORIG'] = env['CXX']
        env['CXX'] = join(self.ctx.root_dir, "tools", "cpplink")

        # setuptools uses CC for compiling and CXX for linking
        env['CC'] = env['CXX']
        env['CFLAGS'] += ' -isysroot {}'.format(env['IOSSDKROOT'])
        return env

recipe = KiwiSolverRecipe()

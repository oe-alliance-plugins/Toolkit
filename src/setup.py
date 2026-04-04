from setuptools import setup
import setup_translate

pkg = 'SystemPlugins.Toolkit'
setup(name='enigma2-plugin-systemplugins-toolkit',
       version='3.0',
       description='common reusable tools for enigma2 plugins',
       package_dir={pkg: 'Toolkit'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'maintainer.info', 'LICENSE']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )

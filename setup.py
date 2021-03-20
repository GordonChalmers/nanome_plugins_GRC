import pathlib
from setuptools import find_packages, setup

README = (pathlib.Path(__file__).parent / "README.md").read_text()

setup(
	name = 'nanome-GlycamCB',
	packages=find_packages(),
	version = '1.0.1',
	license='MIT',
	description = 'Nanome Plugin for the Glycam carbohydrate builder.',
	long_description = README,
        long_description_content_type = "text/markdown",
	author = 'Nanome',
	author_email = 'hello@nanome.ai',
	url = 'https://github.com/gordonchalmers/nanome_plugins/',
	platforms="any",
	keywords = ['virtual-reality', 'chemistry', 'python', 'api', 'plugin'],
	install_requires=['nanome', 'numpy', 'scipy'],
	entry_points={"console_scripts": ["nanome-GlycamCB = nanome_GlycamCB.GlycamCB:main"]},
	classifiers=[
		'Development Status :: 3 - Alpha',

		'Intended Audience :: Science/Research',
		'Topic :: Scientific/Engineering :: Chemistry',

		'License :: OSI Approved :: MIT License',

		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
	],
	package_data={
        "nanome_GlycamCB": [
            "*.json",
			"*.png"
        ]
	},
)

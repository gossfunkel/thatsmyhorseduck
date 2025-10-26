from setuptools import setup

setup(
	name = "thatsmyhorseduck",
	options = {
		'build_apps': {
			# build the exe as a gui_app
			'gui_apps': {
				'thatsmyhorseduck': 'horseduck.py',
			},
			'icons': {
				'thatsmyhorseduck': ["icon-256.png"],
			},

			# output logging
			'log_filename': '$USER_APPDATA/thatsmyhorse/output.log',
			'log_append': False,

			# specify included files
			'include_patterns': [
				'**/**.bam'
				'**/**.png'
			],

			# extensions for automatic .bam conversion
			#'bam_model_extensions': ['.gltf'],

			# opengl renderer
			'plugins': [
				'pandagl',
				'p3openal_audio',
			],
		}
	}
)
from setuptools import setup, find_packages

setup(
	name='Terminal_Digital_Clock',
	version='1.0.0',
	description='Live clock in terminal',
	url='https://github.com/PizzaPat/Terminal_Digital_Clock',
	author='Patrapee Pongtana',
	author_email='patpongtana@gmail.com',
	license='MIT',
	packages=find_packages(),
	keywords=['clock'],
	entry_points={
		'console_scripts':[
			'clock=Terminal_Digital_Clock.digitalClock:main'
			]}
	)
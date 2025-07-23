from setuptools import find_packages, setup

package_name = 'rxjoy_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Bora',
    maintainer_email='NoCosecantOfTheta@gmail.com',
    description='Receive and publish joystick input over network',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "rxjoy_node = rxjoy_pkg.joy_receiver:main",
        ],
    },
)

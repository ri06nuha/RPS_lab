from setuptools import find_packages, setup

package_name = 'exam_pkg'

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
    maintainer='fariza',
    maintainer_email='ri06nuha@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [ 
            'exam_publisher = exam_pkg.exam_publisher:main',
            'simple = exam_pkg.simple:main',
            'quest_3 = exam_pkg.exam_pub:main',
            'exam_sub = exam_pkg.exam_subscriber:main',
            'multi_pub = exam_pkg.multi_pub:main'
        ],
    },
)

from setuptools import setup

package_name = 'drone_movement'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'print_test = drone_movement.print_test:main',
            'offload_control = drone_movement.offload_control:main',
            'orbit_cmd = drone_movement.orbit_cmd:main',
            # 'lim_offboard = drone_movement.lim_offboard:main',
            'boat_publisher = drone_movement.boat_publisher:main',
            'yf_offboard1 = drone_movement.yf_offboard1:main',
            'yf_offboard = drone_movement.yf_offboard:main'
        ],
    },
)

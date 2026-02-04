## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD
## Updated: Support both catkin and pip install

from setuptools import setup, find_packages

# Try to use catkin_pkg if available (for ROS environment)
try:
    from catkin_pkg.python_setup import generate_distutils_setup
    
    # fetch values from package.xml
    setup_args = generate_distutils_setup(
        packages=['ros_numpy'],
        package_dir={'': 'src'})
    
    setup(**setup_args)

except ImportError:
    # Fallback for pip install (non-ROS environment)
    setup(
        name='ros_numpy',
        version='0.0.5',
        description='Tools for converting ROS messages to and from numpy arrays',
        author='Eric Wieser',
        author_email='wieser.eric@gmail.com',
        url='https://github.com/CiRA-AMI/cira_ros_numpy',
        packages=find_packages(where='src'),
        package_dir={'': 'src'},
        install_requires=[
            'numpy',
        ],
        python_requires='>=3.6',
    )

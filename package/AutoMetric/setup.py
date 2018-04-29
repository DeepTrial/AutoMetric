from setuptools import setup, find_packages

setup(
    name='autometric',
    version=0.1,
    description=(
        'draw ROC,PR curve and calculate AUC MAP IoU for image semantic segmentation problem'
    ),
    long_description=open('README.rst').read(),
    author='Resnick Xing',
    author_email='resnick.xing@gmail.com',
    maintainer='Resnick Xing',
    maintainer_email='resnick.xing@gmail.com',
    license='BSD License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/DeepTrial/AutoMetric',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
)
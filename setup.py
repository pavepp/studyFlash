from distutils.core import setup

setup(
    name='studyFlash',
    version='0.5.3',
    description="Learning flashcards inside your terminal",
    author="Alone2",
    author_email="admin@bundr.net",
    url="https://github.com/Alone2/studyFlash",
    packages=['studyFlash'],
    scripts=['scripts/studyflash', 'scripts/studyflash-quizlet']
)
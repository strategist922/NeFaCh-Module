<?xml version="1.0" encoding="UTF-8" ?>
<Package name="nefach" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="." xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs />
    <Resources>
        <File name="icon" src="icon.png" />
        <File name="main" src="scripts/main.py" />
        <File name="__init__" src="scripts/stk/__init__.py" />
        <File name="__init__" src="scripts/stk/__init__.pyc" />
        <File name="events" src="scripts/stk/events.py" />
        <File name="events" src="scripts/stk/events.pyc" />
        <File name="logging" src="scripts/stk/logging.py" />
        <File name="logging" src="scripts/stk/logging.pyc" />
        <File name="runner" src="scripts/stk/runner.py" />
        <File name="runner" src="scripts/stk/runner.pyc" />
        <File name="services" src="scripts/stk/services.py" />
        <File name="services" src="scripts/stk/services.pyc" />
        <File name="swiftswords_ext" src="swiftswords_ext.mp3" />
        <File name="taichimove" src="taichimove.pmt" />
    </Resources>
    <Topics>
        <Topic name="introductions" src="scripts/topic/introductions.top" topicName="" language="" />
    </Topics>
    <IgnoredPaths>
        <Path src=".metadata" />
    </IgnoredPaths>
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>

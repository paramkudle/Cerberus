# Cerberus
Proof of Concept for a Virus which downloads the payload in multiple stages

This is merely a Proof of Concept and should be used for educational purposes only.
Whether or not you evade detection is purely based on your payload.


  

## How does it work?

The malicious code is divided into 3 stages in `TSource` files.

There are 3 Stages divided in `StageSource` files. These files retrieve the code from seperate `TSource` files from seperate specified URLs and append it into a main payload file **part by part**. (Why?)

The 3 Stages can be put into `Cerberus.py`, yes, but this way it is detected almost always.

The main file `Cerberus.py` retrieves the code for the first stage and starts the malware.  


## How to Improve

You can divide the payload into more parts to avoid detection.

One more way to evade detection is by obfuscating both the python files as well.

You can obfuscate and then compile `Cerberus.py` into a .exe by using a [.py to .exe converter.](https://pypi.org/project/auto-py-to-exe/)

Make sure to add a Anti-VM feature in your payload to avoid detection on VirusTotal.

## To-Do:

Arranged according to priority

* Actually make a Good Example Payload
* Implement Polymorphism
* Make a Persisting Malware
* Retrieve Code and Execute in Memory without Writing to Disk.
* Anti-VM/Anti-Sandbox
* Obfuscation (?)
* Server-side encrypt the Code Randomly every 5 minutes with a Key (?)
* Bytecode (?)


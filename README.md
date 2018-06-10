# blockchain-fun
Blockchain Fun

Just having some fun with Blockchain with Peckchain, a pretend system for working with my Peck warehouse management system.
I was inspired by a mini blockchain article I found on Medium, but that article left me with questions, so I had to mess with it myself. :)

Here's what I've done so far:
* Made stuff work, changed some names to what I like.
* Added yaml file support to read my config files
* Fixed a few little bugs in the list blocks code
* Made a Transactor who is sending updates to the blockchain
* 6/9: OK with the commits on 6/9/2018, I started tossing the SnakeCoin stuff out the window and started going my own way reading different blockchain resources.
* 6/10: Replaced the SnakeCoin (divisible by last PoW and 9) with a "next hash starting with 0000"
* 6/10: Hooked up a rudimentary consensus process (a "mine" operation checks for consensus first)
* 6/10: Made the transactor trigger a consensus check from time to time.

TODO:
* Need a better PoW calculation function
* Need to Create different transactions and then do an integrity check
* Query the blockchain for some type of transaction information (e.g. how many coins does each miner own?)
* Simulate a rogue agent adding his own stuff to the chain
* Instructions on how to run it and show how it works
* Understand the part about mining and then getting a "coin", which is leftover from the SnakeCoin demo stuff.  In this blockchain example, you don't need to get a coin, so maybe that goes away.
* Make some kind of timer check to Mine every so often to add new things to the blockchain
* And how come every time a miner mines, it get added to the blockchain (proof of work), even though nothing useful gets added.  That will fill up the blockchain space pretty quickly.  Maybe for a cryptocurrency, this would be important, but not for this application--or am I missing something?
* Add another Miner (maybe configure all of them in one file?  I don't know)
* Make my individual miners compare every so often to each others blockchains to get consensus
* I was thinking i wanted the miner to be a standalone python program, but I don't totally remember why.  Perhaps so the standalone application can create more interesting sample data to add?
* Update the comments
* Commit the code to github more between updates more frequently, so the updates make more sense versus one gigantic code push.

Sources:
* https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b
* https://medium.com/crypto-currently/lets-make-the-tiniest-blockchain-bigger-ac360a328f4d
* https://gist.github.com/aunyks/47d157f8bc7d1829a729c2a6a919c173
* Bitcoin for the Befuddled (a book)

Misc:
* If you want to send me any bitcoins (yeah right!) send them to:
  * BTC Wallet Address: 38LzLXiq16v8BLsmHERnwXdQaJnDM5R5nE
  * BCH Wallet Address: qrwrytprgv4d58r4ekdnswaxqxtwya6a9vl72uhkm6

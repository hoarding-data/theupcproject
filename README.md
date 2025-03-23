# theupcproject
UPC data so people don't need to struggle like me.

## Purpose
This is meant to be a "root" level of UPC data. A lot of UPC projects on the internet have incomplete data (this is no different), but they also tend to have very strange and incomplete data models that they apply to all items (presumably as part of a relational database). Additionally, the data tends to be paywalled or API restricted.

My goal is two-fold:
- Provide the UPC code and a descriptive item name for as many UPCs as possible
- Add an additional "ipfs_cid" field which would point to a pinned (probably json?) object containing more complete information (image links, 3d models, nutrition facts, manuals, etc).

I don't know how to write .md files well so hopefully this isn't formatted too poorly out the gate.

Many people probably want a nice rest API with all that data. I don't want to pay to host that API, deal with trying to rate-limit a free tier, or any of the other headaches that would come with that. If you're willing to pay the main API I'm aware of is [BarcodeLookup](https://www.barcodelookup.com/api). The idea of this is it's free and decentralized, so you can do whatever you want with it (and hopefully one day someone will make a service that I don't need to be hands on with).

## About UPCs
[Read More Here](https://www.barcode-us.info/upc-codes/)
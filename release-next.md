# [NimbusML](https://docs.microsoft.com/en-us/nimbusml/overview) Next

## **New Features**

- **Initial implementation of NGramExtractor.**

    [PR#320](https://github.com/microsoft/NimbusML/pull/320)
    Produces a bag of counts of n-grams (sequences of consecutive values of length 1-n)
    in a given vector of keys. It does so by building a dictionary of n-grams and using
    the id in the dictionary as the index in the bag.

- **Update Manifest Generator.**

    [PR#329](https://github.com/microsoft/NimbusML/pull/329)
    Update the Manifest Generator project to work with the latest changes and incorporate
    it in to the build process.

## **Bug Fixes**

None.

## **Enhancements**

- **Update Tests To Execute In Parallel.**

    [PR#331](https://github.com/microsoft/NimbusML/pull/331)

## **Documentation and Samples**

None. 

## **Remarks**

None.

# Entrypoints

## Background
NimbusML uses ML.NET's [Entrypoints](https://github.com/dotnet/machinelearning/blob/master/docs/code/EntryPoints.md) API to call ML.NET components from python.  The Entrypoints API allows a user working in a non-.NET language to describe a call to an ML.NET estimator or transformer in JSON format and pass the JSON to ML.NET for execution.  So in NimbusML we embed the ML.NET binaries in the published package, expose a python API that constructs these estimator/transformer JSONs, and call the the ML.NET binaries via extension modules to execute the constructed JSONs.

This is implemented in NimbusML by autogenerating python classes for each of the estimators and transformers in ML.NET. These autogenerated classes do not contain the logic of the corresponding ML.NET components, but rather logic to create the appropriate JSON representation for the entrypoint API. 

## Modifying Entrypoint Components and Their Docstrings
These python classes are produced by running [entrypoint_compiler.py](https://github.com/Microsoft/NimbusML/blob/master/src/python/tools/entrypoint_compiler.py), and you will see a comment noting this at the top of each of the files: `# - Generated by tools/entrypoint_compiler.py: do not edit by hand`. If you want to modify the logic of a component, you will have to modify the underlying component in ML.NET.  For example, if you want to edit [kmeansplusplus.py](https://github.com/Microsoft/NimbusML/blob/master/src/python/nimbusml/internal/core/cluster/kmeansplusplus.py), you want to look at ML.NET's [KMeansPlusPlusTrainer.cs](https://github.com/dotnet/machinelearning/blob/master/src/Microsoft.ML.KMeansClustering/KMeansPlusPlusTrainer.cs).

If you want to edit the docstring for a NimbusML component, you likewise cannot directly edit the docstring in the autogenerated file. Entrypoint_compiler.py generates the docstrings in these files from a seperate docstring text file that we maintain in the source repo, and this is the file that must be modified.<sup>[1](#myfootnote1)</sup>  For example, the docstring for [kmeansplusplus.py](https://github.com/Microsoft/NimbusML/blob/master/src/python/nimbusml/internal/core/cluster/kmeansplusplus.py) is generated from [KMeansPlusPlus.txt](https://github.com/Microsoft/NimbusML/blob/master/src/python/docs/docstrings/KMeansPlusPlus.txt). After the changes are made, a modified `kmeansplusplus.py` can be generated by running `entrypoint_compiler.py`.

If you forget and accidently edit one of these classes that are autogenerated, the validation build will catch this and fail when checking to see if the autogenerated files are consistent with the docstring text files and the corresponding ML.NET component.

So the end to end process for editing a docstring is to:
1. Edit [KMeansPlusPlus.txt](https://github.com/Microsoft/NimbusML/blob/master/src/python/docs/docstrings/KMeansPlusPlus.txt).
2. Run [entrypoint_compiler.py](https://github.com/Microsoft/NimbusML/blob/master/src/python/tools/entrypoint_compiler.py) locally with `python entrypoint_compiler.py --generate_api` to produce [kmeansplusplus.py](https://github.com/Microsoft/NimbusML/blob/master/src/python/nimbusml/internal/core/cluster/kmeansplusplus.py) with your change reflected in the docstring.
3. Make a PR with both the edited text file and the edited autogenerated file.


##### Footnotes:

<a name="myfootnote1">1</a>:
The docstrings text file such as KMeansPlusPlus.txt doesn't contain everything. It only contains python docstrings that we want to add in addition to the documentation metadata that comes from ML.NET.  This ML.NET metadata is gathered from [manifest.json](https://github.com/Microsoft/NimbusML/blob/master/src/python/tools/manifest.json).  Sometimes we want to make one-off naming changes to the metadata in manifest.json to make it more pythonic, and we do this in [manifest_diff.json](https://github.com/Microsoft/NimbusML/blob/master/src/python/tools/manifest_diff.json).  So the full list of sources that entrypoint_compiler.py uses to produce our docstrings are:
1. manifest.json (comes directly from ML.NET)
2. manifest_diff.json
3. docstrings txt file (for example src/python/docs/docstrings/KMeansPlusPlus.txt)

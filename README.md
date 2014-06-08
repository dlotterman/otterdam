### Otterdam

Otterdam is a personal POC project. It is intended to solve the "too many things to test" problem associated with benchmarking mature *nix environments in a automated and repeatable way.

It loads a folder of "recipes", each of which is a step in building, executing or tearing down a servers configuration. Each recipe and have multiple flags, the combinations of which are found. Each recipe is the combined with every other recipe and their associated combinations, to create a list of ordered commands to be executed shell.

This means you can have:

`create_disk_command --option_1 (1, 2, 3) --options_2 (a,b) --option_3 (Z)1
`create_network_command --option_1 (a, b)`
`execute_bench_command --option_1 (z, y) --option_2 (9, 8)`

And Otterdamn will discover all the combinations of these commands and execute them as ordered by the recipe.

#### Current Status
Currently works (maybe?) in a limited sandbox way. All recipes must be parseable JSON. It requires python2.6 and the associated standard libraries.


#### TODOs
* De-duplicate commands. Currently, many combinations will cause there to de "duplicate" (`command --option1 --option2`,`command --option2 --option1`) instances of commands in the command list.
* Add support for exclusionary recipes, so allow for once sequence of commands that use `mkfs.xfs` and another that use `mkfs.ext4` but not both.
* Add support for managing config files directly, so allow for config files with specific lines with combinations of strings
* Add support for ssh'ing to remote systems
* Add webscale bootstrap UI for both creation of JSON files as well as monitoring output
* Verify functionality on non Linux *nixs (FreeBSD, Solaris etc)


#### License
GNU GPL 3. Or which ever license allows you to do the most of what ever you want

#### Is it any good?
Not yet but it will be

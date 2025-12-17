# Ultra Make

Ultra Make is a simple assistant built on top of `make`.  
Its goal is to make common Makefile tasks easier and faster.

## Installation

Run the following command:

```bash
bash install.sh
```

After installation, **restart your terminal** to apply the alias.

## Usage

Ultra Make is used through the `umake` alias.

You must run `umake` **inside the directory that contains the Makefile**.

```bash
umake
```

## Arguments

Ultra Make supports multiple arguments:

* `-n`
  Runs Norminette on the project. Make sure it is installed.

* `DEBUG`
  Executes the `DEBUG` rule defined in the Makefile.

Example:

```bash
umake -n DEBUG
```

## Notes

* Ultra Make is currently a work in progress and is developed as a side project during my 42 Common Core.
* For now, `DEBUG` is the only supported Makefile flag.
* Additional features may be added in the future.

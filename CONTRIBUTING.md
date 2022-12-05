# Contributing to the project

## How to contribute

If you want to add a new resource, please follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Add the new resource.
4. Commit the changes.
5. Push the changes to your fork.
6. Create a pull request.

## How to add a new resource

If you want to add a new resource, please follow these steps:

1. Add the new resource to the appropriate section.
2. Add a link to the new resource in the table of contents if needed.
3. Add a description of the new resource.
4. In case of the resource being a fusion 360 file, please add a link to the fusion 360 file, and a link to the rendered image of the file.
5. In case of the resource being a 3D model, please add a link to the 3D model, and a link to the rendered image of the model.
6. Avoid using submodules. If you want to add a submodule, please contact the project maintainers or ask in the [Latamkeys Discord Server](https://discord.gg/latamkeys) in the `#sistemas` channel.

## Naming conventions for resources

#### File names

File names should be in lowercase, and should use underscores to separate words.

#### Image files

Images should be uploaded to image hosting services, such as imgur, and the link to the image should be used in the markdown file instead of uploading the image to the repository.

#### QMK keymaps

In case of the resource being a QMK keymap, please use the following naming convention:

```text
<keyboard>-<layout>-<username>.json
```

If your username contains hyphens, please replace them with underscores. Try to use the same username that you use in the QMK configurator.

Example: `planck-rev6-myth.json`

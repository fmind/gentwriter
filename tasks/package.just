# run package tasks
[group('package')]
package: package-build

# build package constraints
[group('package')]
package-constraints constraints="constraints.txt":
	uv pip compile pyproject.toml --generate-hashes --output-file={{constraints}}

# build package requirements
[group('package')]
package-requirements requirements="requirements.txt":
	uv pip compile pyproject.toml --output-file={{requirements}}

# build python package
[group('package')]
package-build constraints="constraints.txt": clean-build package-constraints
	uv build --build-constraint={{constraints}} --require-hashes --wheel

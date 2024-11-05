class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, authors, license):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.authors = authors
        self.license = license

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def list_help(self, list):
        string = ""
        for l in list:
            string += f" - {l}\n"
        return string

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\n\nAuthors:\n{self.list_help(self.authors)}"
            f"\n\nDependencies:\n{self.list_help((self.dependencies))}"
            f"\n\nDevelopment dependencies:\n{self.list_help(self.dev_dependencies)}"
        )

Gem::Specification.new do |spec|
  spec.name                    = "one-punch-jekyll"
  spec.version                 = "4.24.0"
  spec.authors                 = ["Ming Li"]

  spec.summary                 = %q{A flexible two-column Jekyll theme.}
  spec.homepage                = "https://github.com/fox20431/fox20431.github.io"
  spec.license                 = "MIT"

  spec.metadata["plugin_type"] = "theme"

  spec.files                   = `git ls-files -z`.split("\x0").select do |f|
    f.match(%r{^(assets|_(data|includes|layouts|sass)/|(LICENSE|README|CHANGELOG)((\.(txt|md|markdown)|$)))}i)
  end
end

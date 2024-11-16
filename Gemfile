source "https://rubygems.org"

# Use GitHub Pages gem which contains a specific version of Jekyll
gem "github-pages", group: :jekyll_plugins

# Use the feed plugin
gem "jekyll-feed", "~> 0.12", group: :jekyll_plugins

# Additional gems
# If you want to specify Jekyll, you can uncomment the next line
# gem "jekyll", "~> 4.3.0"

# Windows and JRuby specific gems
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Performance boosters for Windows
gem "wdm", "~> 0.1", :platforms => [:mingw, :x64_mingw, :mswin]
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]
gem 'faraday-retry'

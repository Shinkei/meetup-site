const webpack = require('webpack')

module.exports = (config, env) => {
  config.plugins.unshift(new webpack.DefinePlugin({
    'process.env.API_BASE_URL': JSON.stringify(process.env.API_BASE_URL),
    'process.env.TITLE': JSON.stringify(process.env.TITLE)
  }))
  config.resolve.modules.push('src')
  return config
}

module.exports = {
  entry: ['./my_ext/static/index.js'],
  output: {
    path:require('path').join(__dirname, 'my_ext','static'),
    filename: 'bundle.js'
  },
  mode: 'development'
}
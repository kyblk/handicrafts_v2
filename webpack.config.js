'use strict'
const { VueLoaderPlugin } = require('vue-loader')
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const path = require('path');

module.exports = {
    plugins: [
        new MiniCssExtractPlugin({
            // Options similar to the same options in webpackOptions.output
            // both options are optional
            filename: "[name].css",
            chunkFilename: "[id].css"
        }),
        new VueLoaderPlugin()
    ],
    entry: './handwork/handicrafts/static/js/main.js',
    output: {
        path: path.resolve(__dirname, './handwork/handicrafts/static/dist'),
        filename: 'bundle.js'
    },
    module: {
        rules: [{
            test: /\.css$/,
            use: [{
                    loader: MiniCssExtractPlugin.loader,
                    options: {
                        // you can specify a publicPath here
                        // by default it use publicPath in webpackOptions.output
                        publicPath: '../'
                    }
                },
                "css-loader"
            ]
        },
        {
        test: /\.vue$/,
        use: 'vue-loader'
      }
      ],
    }
};
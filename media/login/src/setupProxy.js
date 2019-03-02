const proxy = require('http-proxy-middleware');
module.exports = function (app) {
    app.use(proxy("/api/**", {
        //target: "https://www.easy-mock.com/mock/5c78cf6c141be85de9c0ad1b/",
        target: "http://localhost:8000/",
        changeOrigin: true,
    }))
}
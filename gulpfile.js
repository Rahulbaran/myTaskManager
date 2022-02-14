const { src, dest, watch, series } = require("gulp");
const scss = require("gulp-sass")(require("sass"));
const postcss = require("gulp-postcss");
const cssnano = require("cssnano");
const prefixer = require("autoprefixer");
const srcMaps = require("gulp-sourcemaps");
const terser = require("gulp-terser");

// scss Watch task
const scssTask = function () {
  return src("./task_manager/static/scss/*.scss")
    .pipe(srcMaps.init())
    .pipe(scss())
    .pipe(postcss([cssnano(), prefixer()]))
    .pipe(srcMaps.write("."))
    .pipe(dest("./task_manager/static/css"));
};

// JS Watch Task
const JSTask = function () {
  return src("./task_manager/static/js/*.js")
    .pipe(srcMaps.init())
    .pipe(terser())
    .pipe(srcMaps.write("."))
    .pipe(dest("./task_manager/static/minjs"));
};

// watch Task
const watchTask = function () {
  watch("./task_manager/static/scss/*.scss", scssTask);
  watch("./task_manager/static/js/*.js", JSTask);
};

exports.default = series(scssTask, JSTask, watchTask);

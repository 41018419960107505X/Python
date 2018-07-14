(window["webpackJsonp"] = window["webpackJsonp"] || []).push([["common"],{

/***/ "./src/app/utils/storage.ts":
/*!**********************************!*\
  !*** ./src/app/utils/storage.ts ***!
  \**********************************/
/*! exports provided: sessionstorage, localstorage */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "sessionstorage", function() { return sessionstorage; });
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "localstorage", function() { return localstorage; });
var Storage = /** @class */ (function () {
    function Storage(storage) {
        this.storage = storage;
        this.storage = storage;
    }
    Storage.prototype.get = function (key) {
        return this.storage.getItem(key);
    };
    Storage.prototype.set = function (key, value) {
        this.storage.setItem(key, value);
        return true;
    };
    Storage.prototype.clear = function () {
        this.storage.clear();
    };
    Storage.prototype.remove = function (key) {
        this.storage.removeItem(key);
    };
    return Storage;
}());
var sessionstorage = new Storage(window.sessionStorage);
var localstorage = new Storage(window.localStorage);


/***/ })

}]);
//# sourceMappingURL=common.js.map
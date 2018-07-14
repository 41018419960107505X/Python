(window["webpackJsonp"] = window["webpackJsonp"] || []).push([["common-common-module"],{

/***/ "./src/app/common/common-routing.module.ts":
/*!*************************************************!*\
  !*** ./src/app/common/common-routing.module.ts ***!
  \*************************************************/
/*! exports provided: CommonRoutingModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "CommonRoutingModule", function() { return CommonRoutingModule; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
/* harmony import */ var _common_component__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./common.component */ "./src/app/common/common.component.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};



var adminRoutes = [
    {
        path: '',
        component: _common_component__WEBPACK_IMPORTED_MODULE_2__["CommonComponent"]
    }
];
var CommonRoutingModule = /** @class */ (function () {
    function CommonRoutingModule() {
    }
    CommonRoutingModule = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["NgModule"])({
            imports: [
                _angular_router__WEBPACK_IMPORTED_MODULE_1__["RouterModule"].forChild(adminRoutes)
            ],
            exports: [
                _angular_router__WEBPACK_IMPORTED_MODULE_1__["RouterModule"]
            ]
        })
    ], CommonRoutingModule);
    return CommonRoutingModule;
}());



/***/ }),

/***/ "./src/app/common/common.component.css":
/*!*********************************************!*\
  !*** ./src/app/common/common.component.css ***!
  \*********************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = ".header {\n  top: 0;\n  left: 0;\n  width: 100%;\n  z-index: 10000;\n  position: fixed;\n  height: 60px;\n  line-height: 60px;\n  background-color: black;\n}\n.header .btns {\n  float: right;\n  height: 60px;\n}\n.footer {\n  height: 500px;\n}\n"

/***/ }),

/***/ "./src/app/common/common.component.html":
/*!**********************************************!*\
  !*** ./src/app/common/common.component.html ***!
  \**********************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<div class=\"header\">\n    asdfas\n</div>\n<div class=\"content\">\n    <router-outlet></router-outlet>\n</div>\n<div class=\"footer\"></div>\n"

/***/ }),

/***/ "./src/app/common/common.component.ts":
/*!********************************************!*\
  !*** ./src/app/common/common.component.ts ***!
  \********************************************/
/*! exports provided: CommonComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "CommonComponent", function() { return CommonComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};

var CommonComponent = /** @class */ (function () {
    function CommonComponent() {
    }
    CommonComponent.prototype.get = function () {
    };
    CommonComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'common-root',
            template: __webpack_require__(/*! ./common.component.html */ "./src/app/common/common.component.html"),
            styles: [__webpack_require__(/*! ./common.component.css */ "./src/app/common/common.component.css")]
        }),
        __metadata("design:paramtypes", [])
    ], CommonComponent);
    return CommonComponent;
}());



/***/ }),

/***/ "./src/app/common/common.module.ts":
/*!*****************************************!*\
  !*** ./src/app/common/common.module.ts ***!
  \*****************************************/
/*! exports provided: CommonModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "CommonModule", function() { return CommonModule; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _common_routing_module__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./common-routing.module */ "./src/app/common/common-routing.module.ts");
/* harmony import */ var _common_component__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./common.component */ "./src/app/common/common.component.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};



var CommonModule = /** @class */ (function () {
    function CommonModule() {
    }
    CommonModule = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["NgModule"])({
            declarations: [
                _common_component__WEBPACK_IMPORTED_MODULE_2__["CommonComponent"]
            ],
            imports: [
                _common_routing_module__WEBPACK_IMPORTED_MODULE_1__["CommonRoutingModule"]
            ],
            providers: [],
            bootstrap: [_common_component__WEBPACK_IMPORTED_MODULE_2__["CommonComponent"]]
        })
    ], CommonModule);
    return CommonModule;
}());



/***/ })

}]);
//# sourceMappingURL=common-common-module.js.map
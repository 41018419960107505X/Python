(window["webpackJsonp"] = window["webpackJsonp"] || []).push([["customer-customer-module"],{

/***/ "./src/app/customer/customer-routing.module.ts":
/*!*****************************************************!*\
  !*** ./src/app/customer/customer-routing.module.ts ***!
  \*****************************************************/
/*! exports provided: CustomerRoutingModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "CustomerRoutingModule", function() { return CustomerRoutingModule; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
/* harmony import */ var _customer_component__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./customer.component */ "./src/app/customer/customer.component.ts");
/* harmony import */ var _index_index_component__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./index/index.component */ "./src/app/customer/index/index.component.ts");
/* harmony import */ var _questionnaire_form_questionnaire_form_component__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./questionnaire-form/questionnaire-form.component */ "./src/app/customer/questionnaire-form/questionnaire-form.component.ts");
/* harmony import */ var _questionnaire_view_questionnaire_view_component__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./questionnaire-view/questionnaire-view.component */ "./src/app/customer/questionnaire-view/questionnaire-view.component.ts");
/* harmony import */ var _setting_setting_component__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./setting/setting.component */ "./src/app/customer/setting/setting.component.ts");
/* harmony import */ var _wallet_wallet_component__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./wallet/wallet.component */ "./src/app/customer/wallet/wallet.component.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};








var customerRoutes = [
    {
        path: '',
        component: _customer_component__WEBPACK_IMPORTED_MODULE_2__["CustomerComponent"],
        children: [
            {
                path: '',
                component: _index_index_component__WEBPACK_IMPORTED_MODULE_3__["IndexComponent"]
            },
            {
                path: 'questionnaire-form',
                component: _questionnaire_form_questionnaire_form_component__WEBPACK_IMPORTED_MODULE_4__["QuestionnaireFormComponent"]
            },
            {
                path: 'questionnaire-view',
                component: _questionnaire_view_questionnaire_view_component__WEBPACK_IMPORTED_MODULE_5__["QuestionnaireViewComponent"]
            },
            {
                path: 'setting',
                component: _setting_setting_component__WEBPACK_IMPORTED_MODULE_6__["SettingComponent"]
            },
            {
                path: 'wallet',
                component: _wallet_wallet_component__WEBPACK_IMPORTED_MODULE_7__["WalletComponent"]
            }
        ]
    }
];
var CustomerRoutingModule = /** @class */ (function () {
    function CustomerRoutingModule() {
    }
    CustomerRoutingModule = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["NgModule"])({
            imports: [
                _angular_router__WEBPACK_IMPORTED_MODULE_1__["RouterModule"].forChild(customerRoutes)
            ],
            exports: [
                _angular_router__WEBPACK_IMPORTED_MODULE_1__["RouterModule"]
            ]
        })
    ], CustomerRoutingModule);
    return CustomerRoutingModule;
}());



/***/ }),

/***/ "./src/app/customer/customer.component.css":
/*!*************************************************!*\
  !*** ./src/app/customer/customer.component.css ***!
  \*************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = ".header {\n  top: 0;\n  left: 0;\n  width: 100%;\n  position: fixed;\n  height: 50px;\n  line-height: 50px;\n  background-color: white;\n  box-shadow: 0 1px 5px silver;\n  z-index: 10000;\n}\n.header .right {\n  text-align: right;\n  float: right;\n  width: 300px;\n}\n.header .right .item {\n  margin-right: 5px;\n  padding-left: 10px;\n  padding-right: 10px;\n  cursor: pointer;\n  border-right: solid silver 1px;\n  border-radius: 0px;\n}\n.header .right .item:hover {\n  color: #3da8f5;\n}\n.header .right .item:last-child {\n  border-right: none;\n}\n.header .right .item:active {\n  outline: none;\n}\n.header .right .item:focus {\n  outline: none;\n}\n.content {\n  margin-top: 60px;\n}\n.footer {\n  min-height: 200px;\n}\n"

/***/ }),

/***/ "./src/app/customer/customer.component.html":
/*!**************************************************!*\
  !*** ./src/app/customer/customer.component.html ***!
  \**************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<div class=\"header\">\n    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n    <span (click)=\"back()\">\n        <i class=\"fa fa-arrow-left\"></i>&nbsp;后退</span>\n    <div class=\"right\">\n        <span class=\"item\" routerLink=\"/customer/\">问卷</span>\n        <span class=\"item\" routerLink=\"/customer/wallet\">钱包</span>\n        <span class=\"item\" routerLink=\"/customer/setting\">设置</span>\n        <span class=\"item\" (click)=\"logout()\">退出</span>\n    </div>\n</div>\n<div class=\"content container\">\n    <router-outlet></router-outlet>\n</div>\n<div class=\"footer\"></div>"

/***/ }),

/***/ "./src/app/customer/customer.component.ts":
/*!************************************************!*\
  !*** ./src/app/customer/customer.component.ts ***!
  \************************************************/
/*! exports provided: CustomerComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "CustomerComponent", function() { return CustomerComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
/* harmony import */ var _utils_ajax__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../utils/ajax */ "./src/app/utils/ajax.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};



var CustomerComponent = /** @class */ (function () {
    function CustomerComponent(router) {
        this.router = router;
    }
    CustomerComponent.prototype.get = function () {
    };
    CustomerComponent.prototype.back = function () {
        window.history.back();
    };
    CustomerComponent.prototype.logout = function () {
        var _this = this;
        var that = this;
        var ajax = new _utils_ajax__WEBPACK_IMPORTED_MODULE_2__["Ajax"]();
        ajax.success = function (data) {
            _this.router.navigateByUrl('/');
        };
        ajax.delete('/api/v1/session', {});
    };
    CustomerComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'customer-root',
            template: __webpack_require__(/*! ./customer.component.html */ "./src/app/customer/customer.component.html"),
            styles: [__webpack_require__(/*! ./customer.component.css */ "./src/app/customer/customer.component.css")]
        }),
        __metadata("design:paramtypes", [_angular_router__WEBPACK_IMPORTED_MODULE_1__["Router"]])
    ], CustomerComponent);
    return CustomerComponent;
}());



/***/ }),

/***/ "./src/app/customer/customer.module.ts":
/*!*********************************************!*\
  !*** ./src/app/customer/customer.module.ts ***!
  \*********************************************/
/*! exports provided: CustomerModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "CustomerModule", function() { return CustomerModule; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_common__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/common */ "./node_modules/@angular/common/fesm5/common.js");
/* harmony import */ var _angular_forms__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/forms */ "./node_modules/@angular/forms/fesm5/forms.js");
/* harmony import */ var _customer_routing_module__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./customer-routing.module */ "./src/app/customer/customer-routing.module.ts");
/* harmony import */ var _customer_component__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./customer.component */ "./src/app/customer/customer.component.ts");
/* harmony import */ var _index_index_component__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./index/index.component */ "./src/app/customer/index/index.component.ts");
/* harmony import */ var _questionnaire_form_questionnaire_form_component__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./questionnaire-form/questionnaire-form.component */ "./src/app/customer/questionnaire-form/questionnaire-form.component.ts");
/* harmony import */ var _questionnaire_view_questionnaire_view_component__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./questionnaire-view/questionnaire-view.component */ "./src/app/customer/questionnaire-view/questionnaire-view.component.ts");
/* harmony import */ var _setting_setting_component__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ./setting/setting.component */ "./src/app/customer/setting/setting.component.ts");
/* harmony import */ var _wallet_wallet_component__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! ./wallet/wallet.component */ "./src/app/customer/wallet/wallet.component.ts");
/* harmony import */ var _walletflow_walletflow_component__WEBPACK_IMPORTED_MODULE_10__ = __webpack_require__(/*! ./walletflow/walletflow.component */ "./src/app/customer/walletflow/walletflow.component.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};











var CustomerModule = /** @class */ (function () {
    function CustomerModule() {
    }
    CustomerModule = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["NgModule"])({
            declarations: [
                _customer_component__WEBPACK_IMPORTED_MODULE_4__["CustomerComponent"],
                _index_index_component__WEBPACK_IMPORTED_MODULE_5__["IndexComponent"],
                _questionnaire_form_questionnaire_form_component__WEBPACK_IMPORTED_MODULE_6__["QuestionnaireFormComponent"],
                _questionnaire_view_questionnaire_view_component__WEBPACK_IMPORTED_MODULE_7__["QuestionnaireViewComponent"],
                _setting_setting_component__WEBPACK_IMPORTED_MODULE_8__["SettingComponent"],
                _wallet_wallet_component__WEBPACK_IMPORTED_MODULE_9__["WalletComponent"],
                _walletflow_walletflow_component__WEBPACK_IMPORTED_MODULE_10__["WalletFlowComponent"],
            ],
            imports: [
                _angular_common__WEBPACK_IMPORTED_MODULE_1__["CommonModule"],
                _angular_forms__WEBPACK_IMPORTED_MODULE_2__["FormsModule"],
                _customer_routing_module__WEBPACK_IMPORTED_MODULE_3__["CustomerRoutingModule"],
            ],
            providers: [],
            bootstrap: [_customer_component__WEBPACK_IMPORTED_MODULE_4__["CustomerComponent"]]
        })
    ], CustomerModule);
    return CustomerModule;
}());



/***/ }),

/***/ "./src/app/customer/index/index.component.css":
/*!****************************************************!*\
  !*** ./src/app/customer/index/index.component.css ***!
  \****************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = ".white-space {\n  height: 30px;\n}\n.projects {\n  position: relative;\n}\n.projects .utils {\n  text-align: right;\n}\n.projects .utils .glyphicon {\n  cursor: pointer;\n}\n.projects .utils .filters .filter {\n  margin-right: 8px;\n}\n.projects .project {\n  border: solid lightgray 1px;\n  position: relative;\n  margin-top: 5px;\n  padding: 10px 15px;\n  border-radius: 2px;\n}\n.projects .project:hover {\n  box-shadow: 0 1px 2px lightgray;\n  z-index: 1;\n}\n.projects .project .utils {\n  text-align: right;\n}\n.projects .project .utils span {\n  margin-right: 8px;\n}\n.projects .add-project {\n  cursor: pointer;\n}\n.projects .add-project .new-form {\n  margin-top: 10px;\n}\n.projects .add-project .new-form input {\n  border: none;\n  outline: none;\n  border-bottom: solid silver 2px;\n}\n.projects .add-project .new-form input:focus {\n  border-bottom: solid green 2px;\n}\n.projects .add-project .btns {\n  margin-top: 10px;\n}\n.projects .add-project .btns div {\n  text-align: center;\n}\n"

/***/ }),

/***/ "./src/app/customer/index/index.component.html":
/*!*****************************************************!*\
  !*** ./src/app/customer/index/index.component.html ***!
  \*****************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<div class=\"white-space\"></div>\n<div class=\"projects\">\n    <div class=\"utils\">\n        <span class=\"filters\">\n            <span *ngFor=\"let filter of filters\" class='filter btn-sm btn btn-default' [class.btn-primary]=\"filter.active\" (click)=\"query(filter)\">{{filter.name}}</span>\n        </span>\n        <span>总页数: {{pages}}</span>\n        &nbsp;&nbsp;\n        <span>\n            每页数量\n            <select name=\"\" [(ngModel)]=\"query_limit\" (change)=\"change_limit()\">\n                <option value=\"15\">15</option>\n                <option value=\"25\">25</option>\n                <option value=\"35\">35</option>\n            </select>\n        </span>\n        &nbsp;&nbsp; 第 {{query_page}} 页 &nbsp;&nbsp;\n        <i class=\"glyphicon glyphicon-chevron-left\" title=\"上一页\" (click)=\"pre_page()\"></i>\n        &nbsp;&nbsp;\n        <i class=\"glyphicon glyphicon-chevron-right\" title=\"下一页\" (click)=\"next_page()\"></i>\n    </div>\n    <div class=\"white-space\"></div>\n    <div class=\"project row\" *ngFor=\"let item of questionnaires;let index=index\">\n        <div class=\"col-md-10 col-sm-10 col-xs-8\">\n            {{item.create_date}}&nbsp;&nbsp;&nbsp;&nbsp;{{item.title}}\n        </div>\n        <div class=\"utils col-md-2 col-sm-2 col-xs-4\">\n            <span class=\"btn btn-xs btn-info\" title=\"修改\" *ngIf=\"item.state!=1 && item.state!=4\" (click)=\"edit(index)\">\n                <i class=\"glyphicon glyphicon-pencil\"></i>\n            </span>\n            <span class=\"btn btn-xs btn-danger\" title=\"删除\" *ngIf=\"item.state!=1 && item.state!=4\" (click)=\"delete(index)\">\n                <i class=\"glyphicon glyphicon-trash\"></i>\n            </span>\n            <span class=\"btn btn-xs btn-success\" title=\"发布\" *ngIf=\"item.state===3\" (click)=\"publish(index)\">\n                <i class=\"glyphicon glyphicon-pushpin\"></i>\n            </span>\n            <span class=\"btn btn-xs btn-success\" title=\"查看\" *ngIf=\"item.state===4\" (click)=\"view(index)\">\n                <i class=\"fa fa-eye\"></i>\n            </span>\n\n        </div>\n    </div>\n    <div class=\"project row\" *ngIf=\"questionnaires.length==0 && query_state!=0\">\n        没有问卷\n    </div>\n    <div class=\"add-project project row\" *ngIf=\"query_state==0\">\n        <div class=\"col-md-12\" (click)=\"show_new_form=!show_new_form\">添加问卷</div>\n        <div class=\"col-md-12 new-form\" *ngIf=\"show_new_form\">\n            <div class=\"row\">\n                <div class=\"col-md-4 col-sm-12\">\n                    标题:\n                    <input type=\"text\" name=\"title\" [(ngModel)]=\"new_questionnaire.title\">\n                </div>\n                <div class=\"col-md-4 col-sm-12\">\n                    截止日期:\n                    <input type=\"text\" name=\"deadline\" [(ngModel)]=\"new_questionnaire.deadline\" placeholder=\"YYYY-m-d\">\n                </div>\n                <div class=\"col-md-4 col-sm-12\">\n                    数量:\n                    <input type=\"text\" name=\"quantity\" [(ngModel)]=\"new_questionnaire.quantity\">\n                </div>\n            </div>\n            <div class=\"row btns\">\n                <div class=\"col-md-4 col-sm-3 col-xs-12\">\n                </div>\n                <div class=\"col-md-4 col-sm-6 col-xs-12\">\n                    <span class=\"btn btn-primary\" (click)=\"put()\">确认</span>\n                    &nbsp;&nbsp;&nbsp;&nbsp;\n                    <span class=\"btn btn-default\" (click)=\"show_new_form=false\">取消</span>\n                </div>\n                <div class=\"col-md-4 col-sm-3 col-xs-12\">\n                </div>\n            </div>\n        </div>\n    </div>\n</div>\n"

/***/ }),

/***/ "./src/app/customer/index/index.component.ts":
/*!***************************************************!*\
  !*** ./src/app/customer/index/index.component.ts ***!
  \***************************************************/
/*! exports provided: IndexComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "IndexComponent", function() { return IndexComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
/* harmony import */ var _utils_ajax__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../../utils/ajax */ "./src/app/utils/ajax.ts");
/* harmony import */ var _utils_storage__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../../utils/storage */ "./src/app/utils/storage.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};




var IndexComponent = /** @class */ (function () {
    function IndexComponent(router) {
        this.router = router;
        this.filters = [
            {
                active: true,
                class: 'default',
                name: '草稿',
                state: 0
            },
            {
                active: false,
                class: 'warning',
                name: '待审核',
                state: 1
            },
            {
                active: false,
                class: 'danger',
                name: '审核失败',
                state: 2
            },
            {
                active: false,
                class: 'success',
                name: '审核通过',
                state: 3
            },
            {
                active: false,
                class: 'info',
                name: '已发布',
                state: 4
            },
        ];
        this.api = '/api/v1/customer_questionnaire';
        this.pages = 10;
        this.query_state = 0;
        this.query_limit = 15;
        this.query_page = 1;
        this.questionnaires = [];
        this.now = new Date();
        this.show_new_form = false;
        this.new_questionnaire = {
            title: '',
            deadline: this.now.getFullYear() + '-' + (this.now.getMonth() + 1) + '-' + this.now.getDate(),
            quantity: 100
        };
    }
    IndexComponent.prototype.ngOnInit = function () {
        this.get();
    };
    IndexComponent.prototype.query = function (filter) {
        for (var _i = 0, _a = this.filters; _i < _a.length; _i++) {
            var item = _a[_i];
            item.active = false;
        }
        filter.active = true;
        this.query_page = 1;
        this.query_state = filter.state;
        this.get();
    };
    IndexComponent.prototype.change_limit = function () {
        this.query_page = 1;
        this.get();
    };
    IndexComponent.prototype.pre_page = function () {
        this.query_page -= 1;
        if (this.query_page < 1) {
            this.query_page += 1;
            return;
        }
        this.get();
    };
    IndexComponent.prototype.next_page = function () {
        this.query_page += 1;
        if (this.query_page > this.pages) {
            this.query_page -= 1;
            return;
        }
        this.get();
    };
    // 查询问卷
    IndexComponent.prototype.get = function () {
        var that = this;
        var ajax = new _utils_ajax__WEBPACK_IMPORTED_MODULE_2__["Ajax"]();
        var query_data = {
            limit: that.query_limit,
            state: that.query_state,
            page: that.query_page,
        };
        ajax.success = function (data) {
            console.log(data);
            that.questionnaires = data.objs;
            that.pages = data.pages;
        };
        ajax.get(that.api, query_data);
    };
    // 删除问卷
    IndexComponent.prototype.delete = function (index) {
        var that = this;
        var ensure = window.confirm('确认删除吗?');
        if (ensure) {
            var ajax = new _utils_ajax__WEBPACK_IMPORTED_MODULE_2__["Ajax"]();
            ajax.success = function (data) {
                alert('删除成功!');
                that.questionnaires.splice(index, 1);
            };
            ajax.delete(that.api, {
                ids: [that.questionnaires[index].id]
            });
        }
    };
    // 新增问卷
    IndexComponent.prototype.put = function () {
        var that = this;
        var ajax = new _utils_ajax__WEBPACK_IMPORTED_MODULE_2__["Ajax"]();
        ajax.success = function (data) {
            that.get();
            that.show_new_form = false;
        };
        ajax.put(that.api, that.new_questionnaire);
    };
    // 编辑问卷
    IndexComponent.prototype.edit = function (index) {
        _utils_storage__WEBPACK_IMPORTED_MODULE_3__["sessionstorage"].set('questionnaire_id', this.questionnaires[index].id);
        this.router.navigateByUrl('/customer/questionnaire-form');
    };
    // 发布问卷
    IndexComponent.prototype.publish = function (index) {
        var that = this;
        var ajax = new _utils_ajax__WEBPACK_IMPORTED_MODULE_2__["Ajax"]();
        ajax.success = function (data) {
            alert('发布成功!');
            that.questionnaires.splice(index, 1);
        };
        ajax.put('/api/v1/questionnaire_state', {
            questionnaire_id: that.questionnaires[index].id
        });
    };
    // 查看问卷
    IndexComponent.prototype.view = function (index) {
        _utils_storage__WEBPACK_IMPORTED_MODULE_3__["sessionstorage"].set('questionnaire_id', this.questionnaires[index].id);
        this.router.navigateByUrl('/customer/questionnaire-view');
    };
    IndexComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'customer-index',
            template: __webpack_require__(/*! ./index.component.html */ "./src/app/customer/index/index.component.html"),
            styles: [__webpack_require__(/*! ./index.component.css */ "./src/app/customer/index/index.component.css")]
        }),
        __metadata("design:paramtypes", [_angular_router__WEBPACK_IMPORTED_MODULE_1__["Router"]])
    ], IndexComponent);
    return IndexComponent;
}());



/***/ }),

/***/ "./src/app/customer/questionnaire-form/questionnaire-form.component.css":
/*!******************************************************************************!*\
  !*** ./src/app/customer/questionnaire-form/questionnaire-form.component.css ***!
  \******************************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = ".white-space {\n  height: 30px;\n}\n.save-btn {\n  display: inline-block;\n  width: 50px;\n  height: 50px;\n  line-height: 50px;\n  text-align: center;\n  border-radius: 50%;\n  background-color: #e2e0e0;\n  color: gray;\n  position: fixed;\n  top: 70px;\n  right: 90px;\n  cursor: pointer;\n  z-index: 100;\n  box-shadow: 0px 1px 3px silver;\n}\n.save-btn:hover {\n  background-color: silver;\n  color: black;\n}\n.comment-btn {\n  display: inline-block;\n  width: 50px;\n  height: 50px;\n  line-height: 50px;\n  text-align: center;\n  border-radius: 50%;\n  background-color: #337ab7;\n  color: white;\n  box-shadow: 0px 1px 3px silver;\n  position: fixed;\n  top: 70px;\n  right: 20px;\n  cursor: pointer;\n  z-index: 100;\n}\n.comment-btn:hover {\n  background-color: #2c6aa0;\n}\ninput {\n  border: none;\n  outline: none;\n  border-bottom: solid silver 2px;\n  padding: 5px;\n}\ninput:focus {\n  border-bottom: solid green 2px;\n}\n.questions .question {\n  margin-top: 15px;\n  position: relative;\n}\n.questions .question .edit-btns {\n  position: absolute;\n  width: 100px;\n  right: 10px;\n  top: 10px;\n}\n.questions .question .edit-btns i {\n  cursor: pointer;\n}\n.questions .question .title input {\n  width: 80%;\n}\n.questions .question .items {\n  padding-left: 30px;\n}\n.questions .question .items input {\n  width: 60%;\n}\n.questions .question .items .item span {\n  display: none;\n}\n.questions .question .items .item:hover span {\n  display: inline;\n}\n.questions .question .items .item i {\n  cursor: pointer;\n}\n.questions .question .add-new-item {\n  padding-right: 20px;\n  margin-top: 10px;\n}\n.questions .question .add-new-item i {\n  cursor: pointer;\n}\n.categorys {\n  margin-top: 20px;\n}\n.categorys .category {\n  margin-right: 10px;\n}\n.comment {\n  margin-top: 60px;\n}\n.comment .title {\n  font-size: 1.2em;\n}\n.comment .comment-history {\n  margin-top: 5px;\n  padding: 10px;\n}\n"

/***/ }),

/***/ "./src/app/customer/questionnaire-form/questionnaire-form.component.html":
/*!*******************************************************************************!*\
  !*** ./src/app/customer/questionnaire-form/questionnaire-form.component.html ***!
  \*******************************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<div class=\"white-space\"></div>\n<span class=\"save-btn\" (click)=\"post_questionnaire(0)\">保存</span>\n<span class=\"comment-btn\" (click)=\"post_questionnaire(1)\">审核</span>\n<div class=\"col-md-12 new-form\">\n    <div class=\"row\">\n        <div class=\"col-md-4 col-sm-12\">\n            标题:\n            <input type=\"text\" name=\"title\" [(ngModel)]=\"questionnaire.title\">\n        </div>\n        <div class=\"col-md-4 col-sm-12\">\n            截止日期:\n            <input type=\"text\" name=\"deadline\" [(ngModel)]=\"questionnaire.deadline\" placeholder=\"YYYY-m-d\">\n        </div>\n        <div class=\"col-md-4 col-sm-12\">\n            数量:\n            <input type=\"text\" name=\"quantity\" [(ngModel)]=\"questionnaire.quantity\">\n        </div>\n    </div>\n</div>\n<div class=\"comment\" *ngIf=\"questionnaire.state===2\">\n    <div class=\"title\">审核历史</div>\n    <div class=\"comment-history\">\n        <div *ngFor=\"let comment of questionnaire.comments;let index=index\">\n            {{index+1}}.&nbsp;{{comment.create_date}}\n            <div>\n                &nbsp;&nbsp;&nbsp;&nbsp;{{comment.comment}}\n            </div>\n        </div>\n        <div *ngIf=\"questionnaire.comments.length===0\">\n            暂无\n        </div>\n    </div>\n</div>\n<div class=\"row questions\">\n    <div class=\"col-md-12\">\n        <div *ngFor=\"let question of questionnaire.questions;let index=index\">\n            <div class=\"question\" *ngIf=\"question.edit\">\n                <div class=\"edit-btns\">\n                    <i class=\"glyphicon glyphicon-ok\" (click)=\"save_question(question,index)\" title=\"保存\"></i>\n                    &nbsp;\n                    <i class=\"glyphicon glyphicon-trash\" (click)=\"delete_question(index)\" title=\"删除\"></i>\n                    &nbsp;\n                    <i class=\"glyphicon glyphicon-arrow-up\" (click)=\"up_question(index)\" title=\"上移\"></i>\n                    &nbsp;\n                    <i class=\"glyphicon glyphicon-arrow-down\" (click)=\"down_question(index)\" title=\"下移\"></i>\n                </div>\n\n                <div class=\"title\">\n                    {{index+1}}.&nbsp;&nbsp;\n                    <span *ngIf=\"question.category==='radio'\">单选</span>\n                    <span *ngIf=\"question.category==='select'\">多选</span>\n                    &nbsp;&nbsp;\n                    <input type=\"title\" name=\"title_{{index}}\" [(ngModel)]=\"question.title\" placeholder=\"问题\">\n                </div>\n                <div class=\"items\">\n                    <div class=\"item\" *ngFor=\"let item of question.items;let itemindex=index\">\n                        {{itemindex+1}}.&nbsp;&nbsp;\n                        <input type=\"text\" name=\"item_{{index}}_{{itemindex}}\" [(ngModel)]=\"item.content\">\n                        <span>\n                            <i class=\"glyphicon glyphicon-arrow-up\" (click)=\"up_question_item(question,itemindex)\"></i>\n                            &nbsp;\n                            <i class=\"glyphicon glyphicon-arrow-down\" (click)=\"down_question_item(question,itemindex)\"></i>\n                            &nbsp;\n                            <i class=\"glyphicon glyphicon-trash\" (click)=\"remove_question_item(question,itemindex)\"></i>\n                        </span>\n                    </div>\n                </div>\n                <div class=\"add-new-item\">\n                    &nbsp; &nbsp; &nbsp; &nbsp;\n                    <i class=\"glyphicon glyphicon-plus\" (click)=\"add_question_item(question)\"></i>\n                </div>\n            </div>\n            <div class=\"question\" *ngIf=\"!question.edit\">\n                <div class=\"edit-btns\">\n                    <i class=\"glyphicon glyphicon-pencil\" (click)=\"edit_question(question)\" title=\"保存\"></i>\n                    &nbsp;\n                    <i class=\"glyphicon glyphicon-trash\" (click)=\"delete_question(index)\" title=\"删除\"></i>\n                    &nbsp;\n                    <i class=\"glyphicon glyphicon-arrow-up\" (click)=\"up_question(index)\" title=\"上移\"></i>\n                    &nbsp;\n                    <i class=\"glyphicon glyphicon-arrow-down\" (click)=\"down_question(index)\" title=\"下移\"></i>\n                </div>\n                <div class=\"title\">\n                    {{index+1}}.&nbsp;&nbsp;\n                    <span *ngIf=\"question.category==='radio'\">单选</span>\n                    <span *ngIf=\"question.category==='select'\">多选</span>\n                    &nbsp;&nbsp;{{question.title}}\n                </div>\n                <div class=\"items\">\n                    <div class=\"item\" *ngFor=\"let item of question.items;let itemindex=index\">\n                        {{itemindex+1}}.&nbsp;&nbsp;{{item.content}}\n                    </div>\n                </div>\n            </div>\n        </div>\n    </div>\n</div>\n<div class=\"row categorys\">\n    <div class=\"col-md-12\">\n        <span class=\"category btn btn-primary btn-sm\" *ngFor=\"let item of categorys\" (click)=\"add_quesiton(item)\">\n            <i class=\"glyphicon glyphicon-plus\"></i>{{item.name}}</span>\n    </div>\n</div>"

/***/ }),

/***/ "./src/app/customer/questionnaire-form/questionnaire-form.component.ts":
/*!*****************************************************************************!*\
  !*** ./src/app/customer/questionnaire-form/questionnaire-form.component.ts ***!
  \*****************************************************************************/
/*! exports provided: QuestionnaireFormComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "QuestionnaireFormComponent", function() { return QuestionnaireFormComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
/* harmony import */ var _utils_ajax__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../../utils/ajax */ "./src/app/utils/ajax.ts");
/* harmony import */ var _utils_storage__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../../utils/storage */ "./src/app/utils/storage.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};




var QuestionnaireFormComponent = /** @class */ (function () {
    function QuestionnaireFormComponent(router) {
        this.router = router;
        // 问卷接口
        this.api = '/api/v1/customer_questionnaire';
        // 问题接口
        this.quetion_api = '/api/v1/customer_question';
        // 问题题号接口
        this.quetion_index_api = '/api/v1/question_index';
        // 问题类型
        this.categorys = [
            {
                name: '单选题',
                category: 'radio'
            },
            {
                name: '多选选题',
                category: 'select'
            },
        ];
        this.now = new Date();
        // 问卷对象
        this.questionnaire = {
            title: '',
            deadline: this.now.getFullYear() + '-' + (this.now.getMonth() + 1) + '-' + this.now.getDate(),
            quantity: 100,
            questions: []
        };
        this.questionnaire_id = _utils_storage__WEBPACK_IMPORTED_MODULE_3__["sessionstorage"].get('questionnaire_id');
    }
    QuestionnaireFormComponent.prototype.ngOnInit = function () {
        this.get_questionnaire();
    };
    QuestionnaireFormComponent.prototype.up_question = function (index) {
        if (index <= 0)
            return;
        var current = this.questionnaire.questions[index];
        var pre = this.questionnaire.questions[index - 1];
        this.questionnaire.questions[index] = pre;
        this.questionnaire.questions[index - 1] = current;
        this.post_question_index(this.questionnaire.questions[index], index);
        this.post_question_index(this.questionnaire.questions[index - 1], index - 1);
    };
    QuestionnaireFormComponent.prototype.down_question = function (index) {
        if (index >= this.questionnaire.questions.length - 1)
            return;
        var current = this.questionnaire.questions[index];
        var next = this.questionnaire.questions[index + 1];
        this.questionnaire.questions[index] = next;
        this.questionnaire.questions[index + 1] = current;
        this.post_question_index(this.questionnaire.questions[index], index);
        this.post_question_index(this.questionnaire.questions[index + 1], index + 1);
    };
    // 修改问题
    QuestionnaireFormComponent.prototype.edit_question = function (question) {
        question.edit = true;
    };
    // 添加问题
    QuestionnaireFormComponent.prototype.add_quesiton = function (item) {
        this.questionnaire.questions.push({
            id: 0,
            title: '',
            category: item.category,
            items: [],
            edit: true
        });
    };
    // 添加问题选项
    QuestionnaireFormComponent.prototype.add_question_item = function (question) {
        question.items.push({
            content: ''
        });
    };
    // 移除问题选项
    QuestionnaireFormComponent.prototype.remove_question_item = function (question, index) {
        question.items.splice(index, 1);
    };
    // 问题选项上移
    QuestionnaireFormComponent.prototype.up_question_item = function (question, index) {
        if (index <= 0)
            return;
        var current = question.items[index];
        var pre = question.items[index - 1];
        question.items[index] = pre;
        question.items[index - 1] = current;
    };
    // 问题选项下移
    QuestionnaireFormComponent.prototype.down_question_item = function (question, index) {
        if (index >= question.items.length - 1)
            return;
        var current = question.items[index];
        var next = question.items[index + 1];
        question.items[index] = next;
        question.items[index + 1] = current;
    };
    // 保存问题
    QuestionnaireFormComponent.prototype.save_question = function (question, index) {
        var ajax = new _utils_ajax__WEBPACK_IMPORTED_MODULE_2__["Ajax"]();
        ajax.success = function (data) {
            if (data.id) {
                question.id = data.id;
            }
            question.edit = false;
        };
        question.index = index;
        question.questionnaire_id = this.questionnaire_id;
        var items = [];
        if (question.id === 0) {
            ajax.put(this.quetion_api, question, false);
        }
        else {
            ajax.post(this.quetion_api, question, false);
        }
    };
    // 删除问题
    QuestionnaireFormComponent.prototype.delete_question = function (index) {
        var question = this.questionnaire.questions[index];
        if (question.id != 0) {
            var ajax = new _utils_ajax__WEBPACK_IMPORTED_MODULE_2__["Ajax"]();
            ajax.delete(this.quetion_api, {
                'ids': [question.id]
            });
        }
        this.questionnaire.questions.splice(index, 1);
    };
    // 更新问题题号
    QuestionnaireFormComponent.prototype.post_question_index = function (question, index) {
        if (question.id != 0) {
            var ajax = new _utils_ajax__WEBPACK_IMPORTED_MODULE_2__["Ajax"]();
            question.index = index;
            question.questionnaire_id = this.questionnaire_id;
            ajax.post(this.quetion_index_api, question, false);
        }
    };
    QuestionnaireFormComponent.prototype.get_questionnaire = function () {
        var that = this;
        var ajax = new _utils_ajax__WEBPACK_IMPORTED_MODULE_2__["Ajax"]();
        var query_data = {
            limit: 1,
            start_id: parseInt(this.questionnaire_id) - 1,
            with_detail: true
        };
        ajax.success = function (data) {
            that.questionnaire = data.objs[0];
        };
        ajax.get(that.api, query_data);
    };
    QuestionnaireFormComponent.prototype.post_questionnaire = function (state) {
        var ajax = new _utils_ajax__WEBPACK_IMPORTED_MODULE_2__["Ajax"]();
        var data = {
            questionnaire_id: this.questionnaire_id,
            title: this.questionnaire.title,
            deadline: this.questionnaire.deadline,
            quantity: this.questionnaire.quantity,
            state: state
        };
        ajax.success = function (data) {
            alert('提交成功!');
            window.history.back();
        };
        ajax.post(this.api, data);
    };
    QuestionnaireFormComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'customer-questionnaire-form',
            template: __webpack_require__(/*! ./questionnaire-form.component.html */ "./src/app/customer/questionnaire-form/questionnaire-form.component.html"),
            styles: [__webpack_require__(/*! ./questionnaire-form.component.css */ "./src/app/customer/questionnaire-form/questionnaire-form.component.css")]
        }),
        __metadata("design:paramtypes", [_angular_router__WEBPACK_IMPORTED_MODULE_1__["Router"]])
    ], QuestionnaireFormComponent);
    return QuestionnaireFormComponent;
}());



/***/ }),

/***/ "./src/app/customer/questionnaire-view/questionnaire-view.component.css":
/*!******************************************************************************!*\
  !*** ./src/app/customer/questionnaire-view/questionnaire-view.component.css ***!
  \******************************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = ".white-space {\n  height: 30px;\n}\n.questions .question {\n  margin-top: 15px;\n  position: relative;\n}\n.questions .question .items {\n  padding-left: 30px;\n}\n.comment {\n  margin-top: 20px;\n}\n.comment .title {\n  font-size: 1.2em;\n}\n.comment .comment-history {\n  margin-top: 5px;\n  padding: 10px;\n}\n.comment .new-comment {\n  margin-top: 20px;\n}\n.comment .new-comment textarea {\n  width: 100%;\n  height: 100px;\n  padding: 10px;\n  border-radius: 5px;\n  resize: none;\n}\n.comment .new-comment textarea:focus {\n  outline: none;\n}\n.comment .comment-btn {\n  text-align: right;\n}\n.comment .comment-btn span {\n  margin-right: 20px;\n}\n"

/***/ }),

/***/ "./src/app/customer/questionnaire-view/questionnaire-view.component.html":
/*!*******************************************************************************!*\
  !*** ./src/app/customer/questionnaire-view/questionnaire-view.component.html ***!
  \*******************************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<div class=\"white-space\"></div>\n<div class=\"col-md-12 new-form\">\n    <div class=\"row\">\n        <div class=\"col-md-4 col-sm-12\">\n            标题:&nbsp;{{questionnaire.title}}\n        </div>\n        <div class=\"col-md-4 col-sm-12\">\n            截止日期:&nbsp;{{questionnaire.deadline}}\n        </div>\n        <div class=\"col-md-4 col-sm-12\">\n            数量:&nbsp;{{questionnaire.quantity}}\n        </div>\n    </div>\n</div>\n<div class=\"row questions\">\n    <div class=\"col-md-12\">\n        <div *ngFor=\"let question of questionnaire.questions;let index=index\">\n            <div class=\"question\">\n                <div class=\"title\">\n                    {{index+1}}.&nbsp;&nbsp;\n                    <span *ngIf=\"question.category==='radio'\">单选</span>\n                    <span *ngIf=\"question.category==='select'\">多选</span>\n                    &nbsp;&nbsp;{{question.title}}\n                </div>\n                <div class=\"items\">\n                    <div class=\"item\" *ngFor=\"let item of question.items;let itemindex=index\">\n                        {{itemindex+1}}.&nbsp;&nbsp;{{item.content}}\n                    </div>\n                </div>\n            </div>\n        </div>\n    </div>\n</div>\n"

/***/ }),

/***/ "./src/app/customer/questionnaire-view/questionnaire-view.component.ts":
/*!*****************************************************************************!*\
  !*** ./src/app/customer/questionnaire-view/questionnaire-view.component.ts ***!
  \*****************************************************************************/
/*! exports provided: QuestionnaireViewComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "QuestionnaireViewComponent", function() { return QuestionnaireViewComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
/* harmony import */ var _utils_ajax__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../../utils/ajax */ "./src/app/utils/ajax.ts");
/* harmony import */ var _utils_storage__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../../utils/storage */ "./src/app/utils/storage.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};




var QuestionnaireViewComponent = /** @class */ (function () {
    function QuestionnaireViewComponent(router) {
        this.router = router;
        // 问卷接口
        this.api = '/api/v1/customer_questionnaire';
        this.now = new Date();
        // 问卷对象
        this.questionnaire = {
            title: '',
            deadline: this.now.getFullYear() + '-' + (this.now.getMonth() + 1) + '-' + this.now.getDate(),
            quantity: 100,
            questions: [],
            comments: []
        };
        this.new_comment = "";
        this.questionnaire_id = _utils_storage__WEBPACK_IMPORTED_MODULE_3__["sessionstorage"].get('questionnaire_id');
    }
    QuestionnaireViewComponent.prototype.ngOnInit = function () {
        this.get_questionnaire();
    };
    // 获取问卷信息
    QuestionnaireViewComponent.prototype.get_questionnaire = function () {
        var that = this;
        var ajax = new _utils_ajax__WEBPACK_IMPORTED_MODULE_2__["Ajax"]();
        var query_data = {
            limit: 1,
            start_id: parseInt(this.questionnaire_id) - 1,
            with_detail: true
        };
        ajax.success = function (data) {
            that.questionnaire = data.objs[0];
        };
        ajax.get(that.api, query_data);
    };
    // 提交审核
    QuestionnaireViewComponent.prototype.comment = function (agree) {
        if (!agree && this.new_comment === '') {
            alert('请填写批注');
            return false;
        }
        var that = this;
        var ajax = new _utils_ajax__WEBPACK_IMPORTED_MODULE_2__["Ajax"]();
        ajax.success = function (data) {
            alert('提交成功');
            window.history.back();
        };
        ajax.put('/api/v1/questionnaire_comment', {
            questionnaire_id: that.questionnaire_id,
            is_agree: agree,
            comment: that.new_comment
        });
    };
    QuestionnaireViewComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'customer-questionnaire-view',
            template: __webpack_require__(/*! ./questionnaire-view.component.html */ "./src/app/customer/questionnaire-view/questionnaire-view.component.html"),
            styles: [__webpack_require__(/*! ./questionnaire-view.component.css */ "./src/app/customer/questionnaire-view/questionnaire-view.component.css")]
        }),
        __metadata("design:paramtypes", [_angular_router__WEBPACK_IMPORTED_MODULE_1__["Router"]])
    ], QuestionnaireViewComponent);
    return QuestionnaireViewComponent;
}());



/***/ }),

/***/ "./src/app/customer/setting/setting.component.css":
/*!********************************************************!*\
  !*** ./src/app/customer/setting/setting.component.css ***!
  \********************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = ".white-space {\n  height: 30px;\n}\n.tabs {\n  list-style: none;\n  border-right: solid silver 1px;\n  padding-right: 8px;\n}\n.tabs li {\n  text-align: right;\n  padding: 5px;\n  cursor: pointer;\n}\n.tabs li.active {\n  color: #1976d2;\n}\n.tabs li:hover {\n  color: #1976d2;\n  background-color: rgba(0, 0, 0, 0.1);\n}\n.form .row {\n  margin-top: 8px;\n}\n.form .row div:first-child {\n  text-align: right;\n  padding: 5px;\n}\n.form input {\n  width: 250px;\n  padding: 3px;\n  border-radius: 3px;\n  border: solid silver 1px;\n}\n.form input:focus {\n  border: solid #1976d2 1px;\n  outline: none;\n}\n.form textarea {\n  width: 400px;\n  height: 150px;\n  padding: 3px;\n  border-radius: 3px;\n  border: solid silver 1px;\n  resize: none;\n}\n.form textarea:focus {\n  border: solid #1976d2 1px;\n  outline: none;\n}\n"

/***/ }),

/***/ "./src/app/customer/setting/setting.component.html":
/*!*********************************************************!*\
  !*** ./src/app/customer/setting/setting.component.html ***!
  \*********************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<div class=\"white-space\"></div>\n<div class=\"container\">\n    <div class=\"row\">\n        <div class=\"col-sm-2 col-xs-6\">\n            <ul class=\"tabs\">\n                <li *ngFor=\"let tab of tabs\" [class.active]=\"tab.active\" (click)=\"active_tab(tab)\">{{tab.name}}</li>\n            </ul>\n        </div>\n        <div class=\"col-sm-10 col-xs-12\" *ngIf=\"tabs[0].active\">\n            <div class=\"form\">\n                <form action=\"\">\n                    <div class=\"row\">\n                        <div class=\"col-sm-2 col-xs-12\">客户名称</div>\n                        <div class=\"col-sm-10 col-xs-12\">\n                            <input type=\"text\" name=\"name\" [(ngModel)]=\"user.name\">\n                        </div>\n                    </div>\n                    <div class=\"row\">\n                        <div class=\"col-sm-2 col-xs-12\">邮箱</div>\n                        <div class=\"col-sm-10 col-xs-12\">\n                            <input type=\"text\" name=\"email\" [(ngModel)]=\"user.email\">\n                        </div>\n                    </div>\n                    <div class=\"row\">\n                        <div class=\"col-sm-2 col-xs-12\">公司名称</div>\n                        <div class=\"col-sm-10 col-xs-12\">\n                            <input type=\"text\" name=\"company\" [(ngModel)]=\"user.company\">\n                        </div>\n                    </div>\n                    <div class=\"row\">\n                        <div class=\"col-sm-2 col-xs-12\">地址</div>\n                        <div class=\"col-sm-10 col-xs-12\">\n                            <input type=\"text\" name=\"address\" [(ngModel)]=\"user.address\">\n                        </div>\n                    </div>\n                    <div class=\"row\">\n                        <div class=\"col-sm-2 col-xs-12\">手机号码</div>\n                        <div class=\"col-sm-10 col-xs-12\">\n                            <input type=\"text\" name=\"phone\" [(ngModel)]=\"user.phone\">\n                        </div>\n                    </div>\n                    <div class=\"row\">\n                        <div class=\"col-sm-2 col-xs-12\">座机</div>\n                        <div class=\"col-sm-10 col-xs-12\">\n                            <input type=\"text\" name=\"mobile\" [(ngModel)]=\"user.mobile\">\n                        </div>\n                    </div>\n                    <div class=\"row\">\n                        <div class=\"col-sm-2 col-xs-12\">QQ</div>\n                        <div class=\"col-sm-10 col-xs-12\">\n                            <input type=\"text\" name=\"qq\" [(ngModel)]=\"user.qq\">\n                        </div>\n                    </div>\n                    <div class=\"row\">\n                        <div class=\"col-sm-2 col-xs-12\">微信号</div>\n                        <div class=\"col-sm-10 col-xs-12\">\n                            <input type=\"text\" name=\"wechat\" [(ngModel)]=\"user.wechat\">\n                        </div>\n                    </div>\n                    <div class=\"row\">\n                        <div class=\"col-sm-2 col-xs-12\">网站地址</div>\n                        <div class=\"col-sm-10 col-xs-12\">\n                            <input type=\"text\" name=\"web\" [(ngModel)]=\"user.web\">\n                        </div>\n                    </div>\n                    <div class=\"row\">\n                        <div class=\"col-sm-2 col-xs-12\">行业</div>\n                        <div class=\"col-sm-10 col-xs-12\">\n                            <input type=\"text\" name=\"industry\" [(ngModel)]=\"user.industry\">\n                        </div>\n                    </div>\n                    <div class=\"row\">\n                        <div class=\"col-sm-2 col-xs-12\">公司简介</div>\n                        <div class=\"col-sm-10 col-xs-12\">\n                            <textarea type=\"text\" name=\"description\" [(ngModel)]=\"user.description\"></textarea>\n                        </div>\n                    </div>\n                    <div class=\"row\">\n                        <div class=\"col-sm-2 col-xs-12\"></div>\n                        <div class=\"col-sm-10 col-xs-12\">\n                            <button class=\"btn btn-primary\" (click)=\"post()\">保存</button>\n                        </div>\n                    </div>\n                </form>\n            </div>\n        </div>\n        <div class=\"col-sm-10 col-xs-12\" *ngIf=\"tabs[1].active\">\n            <div class=\"form\">\n                <form action=\"\">\n                    <div class=\"row\">\n                        <div class=\"col-sm-2 col-xs-12\">密码</div>\n                        <div class=\"col-sm-10 col-xs-12\">\n                            <input type=\"password\" name=\"password\" [(ngModel)]=\"pwd.password\" />\n                        </div>\n                    </div>\n                    <div class=\"row\">\n                        <div class=\"col-sm-2 col-xs-12\">确认密码</div>\n                        <div class=\"col-sm-10 col-xs-12\">\n                            <input type=\"password\" name=\"ensure_password\" [(ngModel)]=\"pwd.ensure_password\" />\n                        </div>\n                    </div>\n                    <div class=\"row\">\n                        <div class=\"col-sm-2 col-xs-12\"></div>\n                        <div class=\"col-sm-10 col-xs-12\">\n                            <button class=\"btn btn-primary\" (click)=\"udpate_password()\">更新</button>\n                        </div>\n                    </div>\n                </form>\n            </div>\n        </div>\n\n    </div>\n\n</div>"

/***/ }),

/***/ "./src/app/customer/setting/setting.component.ts":
/*!*******************************************************!*\
  !*** ./src/app/customer/setting/setting.component.ts ***!
  \*******************************************************/
/*! exports provided: SettingComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "SettingComponent", function() { return SettingComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
/* harmony import */ var _utils_ajax__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../../utils/ajax */ "./src/app/utils/ajax.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};



var SettingComponent = /** @class */ (function () {
    function SettingComponent(router) {
        this.router = router;
        this.user = {
            category: "",
            name: "",
            email: "",
            company: "",
            address: "",
            phone: "",
            mobile: "",
            qq: "",
            wechat: "",
            web: "",
            industry: "",
            description: "",
        };
        this.pwd = {
            password: "",
            ensure_password: ""
        };
        this.tabs = [
            {
                name: "信息",
                active: true,
            },
            {
                name: "密码",
                active: false
            }
        ];
        this.api = '/api/v1/user';
        this.pwd_api = "/api/v1/password";
    }
    SettingComponent.prototype.ngOnInit = function () {
        this.get();
    };
    // 查询问卷
    SettingComponent.prototype.active_tab = function (tab) {
        for (var _i = 0, _a = this.tabs; _i < _a.length; _i++) {
            var item = _a[_i];
            item.active = false;
        }
        tab.active = true;
    };
    SettingComponent.prototype.get = function () {
        var that = this;
        var ajax = new _utils_ajax__WEBPACK_IMPORTED_MODULE_2__["Ajax"]();
        var query_data = {};
        ajax.success = function (data) {
            that.user = data;
        };
        ajax.get(that.api, {});
    };
    SettingComponent.prototype.post = function () {
        var that = this;
        var ajax = new _utils_ajax__WEBPACK_IMPORTED_MODULE_2__["Ajax"]();
        var query_data = {};
        ajax.success = function (data) {
            alert("更新成功");
        };
        ajax.post(that.api, that.user);
    };
    SettingComponent.prototype.udpate_password = function () {
        var that = this;
        var ajax = new _utils_ajax__WEBPACK_IMPORTED_MODULE_2__["Ajax"]();
        var query_data = {};
        ajax.success = function (data) {
            alert("更新成功");
        };
        ajax.post(that.pwd_api, that.pwd);
    };
    SettingComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'customer-setting',
            template: __webpack_require__(/*! ./setting.component.html */ "./src/app/customer/setting/setting.component.html"),
            styles: [__webpack_require__(/*! ./setting.component.css */ "./src/app/customer/setting/setting.component.css")]
        }),
        __metadata("design:paramtypes", [_angular_router__WEBPACK_IMPORTED_MODULE_1__["Router"]])
    ], SettingComponent);
    return SettingComponent;
}());



/***/ }),

/***/ "./src/app/customer/wallet/wallet.component.css":
/*!******************************************************!*\
  !*** ./src/app/customer/wallet/wallet.component.css ***!
  \******************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = ".white-space {\n  height: 30px;\n}\n.tabs {\n  list-style: none;\n  border-right: solid silver 1px;\n  padding-right: 8px;\n}\n.tabs li {\n  text-align: right;\n  padding: 5px;\n  cursor: pointer;\n}\n.tabs li.active {\n  color: #1976d2;\n}\n.tabs li:hover {\n  color: #1976d2;\n  background-color: rgba(0, 0, 0, 0.1);\n}\n.balance {\n  font-size: 18px;\n}\n.put-balance {\n  margin-top: 30px;\n}\n.put-balance input {\n  border-radius: 3px;\n  border: none;\n  outline: none;\n  border: solid silver 2px;\n  text-align: right;\n}\n.put-balance input:focus {\n  border: solid green 2px;\n}\n.payment-select {\n  margin-top: 10px;\n}\n.payment-select .payment {\n  margin-top: 20px;\n}\n.payment-select .payment span {\n  cursor: pointer;\n  margin-left: 20px;\n}\n.payment-select .payment span img {\n  width: 60px;\n  height: 60px;\n}\n.payment-select .payment-qrcode img {\n  width: 150px;\n  height: 150px;\n}\n"

/***/ }),

/***/ "./src/app/customer/wallet/wallet.component.html":
/*!*******************************************************!*\
  !*** ./src/app/customer/wallet/wallet.component.html ***!
  \*******************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<div class=\"white-space\"></div>\n<div class=\"container\">\n    <div class=\"row\">\n        <div class=\"col-sm-2 col-xs-6\">\n            <ul class=\"tabs\">\n                <li *ngFor=\"let tab of tabs\" [class.active]=\"tab.active\" (click)=\"active_tab(tab)\">{{tab.name}}</li>\n            </ul>\n        </div>\n        <div class=\"col-sm-10 col-xs-12\" *ngIf=\"tabs[0].active\">\n            <div class=\"balance\">\n                可用余额: {{wallet.balance}}\n            </div>\n            <div class=\"put-balance\">\n\n                <div>\n                    充值:\n                    <input type=\"text\" name=\"amount\" [(ngModel)]=\"amount\">\n                </div>\n                <div class=\"payment-select\">\n                    支付方式\n                    <div class=\"payment\">\n                        <span class=\"img\" *ngFor=\"let item of payments\" (click)=\"get_qrcode(item.name)\">\n                            <img [src]=\"item.src\" alt=\"\" />\n                        </span>\n                    </div>\n                    <div class=\"payment-qrcode\" *ngIf=\"qrcode\">\n                        扫码支付\n                        <img [src]=\"sanitizer.bypassSecurityTrustResourceUrl('data:image/png;base64,'+qrcode)\" alt=\"\" />\n                    </div>\n                </div>\n            </div>\n        </div>\n        <div class=\"col-sm-10 col-xs-12\" *ngIf=\"tabs[1].active\">\n            <customer-walletflow></customer-walletflow>\n        </div>\n\n    </div>\n\n</div>"

/***/ }),

/***/ "./src/app/customer/wallet/wallet.component.ts":
/*!*****************************************************!*\
  !*** ./src/app/customer/wallet/wallet.component.ts ***!
  \*****************************************************/
/*! exports provided: WalletComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "WalletComponent", function() { return WalletComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
/* harmony import */ var _angular_platform_browser__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/platform-browser */ "./node_modules/@angular/platform-browser/fesm5/platform-browser.js");
/* harmony import */ var _utils_ajax__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ../../utils/ajax */ "./src/app/utils/ajax.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};




var WalletComponent = /** @class */ (function () {
    function WalletComponent(router, sanitizer) {
        this.router = router;
        this.sanitizer = sanitizer;
        this.tabs = [
            {
                name: "我的钱包",
                active: true,
            },
            {
                name: "流水",
                active: false
            }
        ];
        this.amount = "";
        this.payments = [
            {
                name: "alipay",
                src: "/static/images/alipay.png"
            },
            {
                name: "wechatpay",
                src: "/static/images/wechatpay.png"
            }
        ];
        this.wallet = {
            balance: ""
        };
        this.qrcode = "";
        this.api = '/api/v1/wallet';
    }
    WalletComponent.prototype.ngOnInit = function () {
        this.get();
    };
    // 查询问卷
    WalletComponent.prototype.active_tab = function (tab) {
        for (var _i = 0, _a = this.tabs; _i < _a.length; _i++) {
            var item = _a[_i];
            item.active = false;
        }
        tab.active = true;
    };
    WalletComponent.prototype.get = function () {
        var that = this;
        var ajax = new _utils_ajax__WEBPACK_IMPORTED_MODULE_3__["Ajax"]();
        var query_data = {};
        ajax.success = function (data) {
            that.wallet = data;
        };
        ajax.get(that.api, {});
    };
    WalletComponent.prototype.get_qrcode = function (payment) {
        var that = this;
        var ajax = new _utils_ajax__WEBPACK_IMPORTED_MODULE_3__["Ajax"]();
        var data = {
            amount: this.amount,
            payment: payment
        };
        ajax.success = function (data) {
            that.qrcode = data.qrcode;
        };
        ajax.put(that.api, data);
    };
    WalletComponent.prototype.put = function () {
        var that = this;
        var ajax = new _utils_ajax__WEBPACK_IMPORTED_MODULE_3__["Ajax"]();
        var query_data = {};
        ajax.success = function (data) {
            alert("更新成功");
        };
        ajax.put(that.api, that);
    };
    WalletComponent.prototype.get_wallet_flow = function () {
    };
    WalletComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'customer-wallet',
            template: __webpack_require__(/*! ./wallet.component.html */ "./src/app/customer/wallet/wallet.component.html"),
            styles: [__webpack_require__(/*! ./wallet.component.css */ "./src/app/customer/wallet/wallet.component.css")]
        }),
        __metadata("design:paramtypes", [_angular_router__WEBPACK_IMPORTED_MODULE_1__["Router"], _angular_platform_browser__WEBPACK_IMPORTED_MODULE_2__["DomSanitizer"]])
    ], WalletComponent);
    return WalletComponent;
}());



/***/ }),

/***/ "./src/app/customer/walletflow/walletflow.component.css":
/*!**************************************************************!*\
  !*** ./src/app/customer/walletflow/walletflow.component.css ***!
  \**************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = ".white-space {\n  height: 30px;\n}\n.utils {\n  text-align: right;\n}\n.utils .glyphicon {\n  cursor: pointer;\n}\n.utils .filters .filter {\n  margin-right: 8px;\n}\n.history {\n  margin-top: 20px;\n}\n.history table {\n  width: 100%;\n}\n.history table thead {\n  background-color: silver;\n}\n.history table thead td {\n  font-weight: bold;\n  font-size: 1.2em;\n  text-align: center;\n}\n.history table tbody td {\n  text-align: right;\n  padding: 5px;\n}\n"

/***/ }),

/***/ "./src/app/customer/walletflow/walletflow.component.html":
/*!***************************************************************!*\
  !*** ./src/app/customer/walletflow/walletflow.component.html ***!
  \***************************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<div>\n    <div class=\"utils\">\n        <span class=\"filters\">\n            <span *ngFor=\"let filter of filters\" class='filter btn-sm btn btn-default' [class.btn-primary]=\"filter.active\" (click)=\"query(filter)\">{{filter.name}}</span>\n        </span>\n        <span>总页数: {{pages}}</span>\n        &nbsp;&nbsp;\n        <span>\n            每页数量\n            <select name=\"\" [(ngModel)]=\"query_limit\" (change)=\"change_limit()\">\n                <option value=\"15\">15</option>\n                <option value=\"25\">25</option>\n                <option value=\"35\">35</option>\n            </select>\n        </span>\n        &nbsp;&nbsp; 第 {{query_page}} 页 &nbsp;&nbsp;\n        <i class=\"glyphicon glyphicon-chevron-left\" title=\"上一页\" (click)=\"pre_page()\"></i>\n        &nbsp;&nbsp;\n        <i class=\"glyphicon glyphicon-chevron-right\" title=\"下一页\" (click)=\"next_page()\"></i>\n    </div>\n</div>\n<div class=\"history\">\n    <table>\n        <thead>\n            <tr>\n                <td>金额</td>\n                <td>时间</td>\n                <td>操作</td>\n            </tr>\n        </thead>\n        <tbody>\n            <tr *ngFor=\"let item of walletflows\">\n                <td>{{item.amount}}</td>\n                <td>{{item.create_date}}</td>\n                <td>{{item.reason}}</td>\n            </tr>\n        </tbody>\n    </table>\n</div>"

/***/ }),

/***/ "./src/app/customer/walletflow/walletflow.component.ts":
/*!*************************************************************!*\
  !*** ./src/app/customer/walletflow/walletflow.component.ts ***!
  \*************************************************************/
/*! exports provided: WalletFlowComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "WalletFlowComponent", function() { return WalletFlowComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/router */ "./node_modules/@angular/router/fesm5/router.js");
/* harmony import */ var _utils_ajax__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../../utils/ajax */ "./src/app/utils/ajax.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (undefined && undefined.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};



var WalletFlowComponent = /** @class */ (function () {
    function WalletFlowComponent(router) {
        this.router = router;
        this.filters = [
            {
                active: true,
                class: 'default',
                name: '充值',
                direction: 1
            },
            {
                active: false,
                class: 'warning',
                name: '消费',
                direction: 0
            }
        ];
        this.api = '/api/v1/walletflow';
        this.pages = 1;
        this.query_direction = 1;
        this.query_limit = 15;
        this.query_page = 1;
        this.walletflows = [];
    }
    WalletFlowComponent.prototype.ngOnInit = function () {
        this.get();
    };
    WalletFlowComponent.prototype.query = function (filter) {
        for (var _i = 0, _a = this.filters; _i < _a.length; _i++) {
            var item = _a[_i];
            item.active = false;
        }
        filter.active = true;
        this.query_page = 1;
        this.query_direction = filter.direction;
        this.get();
    };
    WalletFlowComponent.prototype.change_limit = function () {
        this.query_page = 1;
        this.get();
    };
    WalletFlowComponent.prototype.pre_page = function () {
        this.query_page -= 1;
        if (this.query_page < 1) {
            this.query_page += 1;
            return;
        }
        this.get();
    };
    WalletFlowComponent.prototype.next_page = function () {
        this.query_page += 1;
        if (this.query_page > this.pages) {
            this.query_page -= 1;
            return;
        }
        this.get();
    };
    // 查询流水
    WalletFlowComponent.prototype.get = function () {
        var that = this;
        var ajax = new _utils_ajax__WEBPACK_IMPORTED_MODULE_2__["Ajax"]();
        var query_data = {
            limit: that.query_limit,
            direction: that.query_direction,
            page: that.query_page,
        };
        ajax.success = function (data) {
            that.walletflows = data.objs;
            that.pages = data.pages;
        };
        ajax.get(that.api, query_data);
    };
    WalletFlowComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'customer-walletflow',
            template: __webpack_require__(/*! ./walletflow.component.html */ "./src/app/customer/walletflow/walletflow.component.html"),
            styles: [__webpack_require__(/*! ./walletflow.component.css */ "./src/app/customer/walletflow/walletflow.component.css")]
        }),
        __metadata("design:paramtypes", [_angular_router__WEBPACK_IMPORTED_MODULE_1__["Router"]])
    ], WalletFlowComponent);
    return WalletFlowComponent;
}());



/***/ })

}]);
//# sourceMappingURL=customer-customer-module.js.map
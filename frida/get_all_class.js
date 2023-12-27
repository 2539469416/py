function hook_dyn_dex() {
    Java.perform(function () {
        var FridaActivity2 = Java.use("com.butsxi.lixbpyde");
        Java.choose("com.fsdkfdjshkj.RegisterActivity", {
            onMatch: function (ins) {
                //console.log(JSON.stringify(ins.getDynamicDexCheck()));
                //获取这个类的名字
                console.log(ins.getDynamicDexCheck().$className);
            }, onComplete: function () {

            }
        });


        //hook 动态加载的dex
        Java.enumerateClassLoaders({
            onMatch: function (loader) {
                try {
                    if (loader.findClass("com.fsdkfdjshkj.RegisterActivity")) {
                        console.log(loader);
                        Java.classFactory.loader = loader;      //切换classloader
                    }
                } catch (error) {

                }

            }, onComplete: function () {

            }
        });

        var DynamicCheck = Java.use("com.fsdkfdjshkj.RegisterActivity");
        DynamicCheck.check.implementation = function (x) {
            console.log("DynamicCheck.check");
            console.log("x is",x)
            //两种方法
            //var byteArray = Java.array('byte', [-29, -127, -118, -29, -126, -127, -29, -127, -89, -29, -127, -88, -29, -127, -122, 33]);
            var StringClass = Java.use("java.lang.String");
            var byteArray = StringClass.$new("おめでとう!").getBytes();

            console.log("value is",byteArray)
            return this.check(byteArray);
        }
    });
}
function crack1() {
    Java.perform(function(){
        var aaa = Java.use("com.fsdkfdjshkj.RegisterActivity")
        console.log("start")
        aaa.b.implementation = function () {
            return true
        }
        aaa.c.implementation = function () {
            return true
        }
        aaa.d.implementation = function () {
            return true
        }
        aaa.e.implementation = function () {
            return true
        }
        aaa.f.implementation = function () {
            return true
        }
        aaa.g.implementation = function () {
            return true
        }
        aaa.h.implementation = function () {
            return true
        }
        aaa.i.implementation = function () {
            return true
        }
        aaa.j.implementation = function () {
            return true
        }
        aaa.k.implementation = function () {
            return true
        }
        aaa.h.implementation = function () {
            return true
        }
        aaa.l.implementation = function () {
            return true
        }
    })

}
function crack1_1(){
   // 利用反射，获取类中的所有method声明，然后字符串拼接去获取到方法名，批量hook
   Java.perform(function(){
   var aaa = Java.use("com.fsdkfdjshkj.RegisterActivity")
   console.log("aaa",aaa.class)
   var methodsList = aaa.class.getDeclaredMethods();
   for (var i = 0; i < methodsList.length; i++){
        var methodName = methodsList[i].getName();
        console.log(methodName);
        aaa[methodName].implementation = function () {
            console.log("hook_multi_function:", this);
            return true;
        }
    }     })
}
function hook_java(){
    Java.perform(function(){
    })
}

function main(){
    hook_java();
    hook_native();
}

function hook_native(){

}
setImmediate(main)

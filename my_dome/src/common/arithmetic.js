import Vue from 'vue'
import de from 'element-ui/src/locale/lang/de'

class Arithmetic {
  static rszzj = 0;  //初始总资金
  static cssz = 0;  //初始市值
  static csbj = 0;  //初始补仓本金
  static getData = (zfl, origMy, jczj, bl, myArr, ysgj, successCallback) => {
    Arithmetic.rszzj = origMy + jczj
    Arithmetic.csbj = jczj
    let gpsl = Arithmetic.gpslInt(origMy, ysgj);  //股票数量
    let payOff = 0;  //补仓
    let payOffArr = 0; //补仓浮动
    let incsRo = 0;  //盈亏比例
    let ccyk = 0;  //持仓盈亏
    let sxf = 0;  //手续费
    let sxfPay = 0;  //手续费
    let zzc = 0;  //结余总资产
    let zzcArr = []; //总金额list
    let bcArr = [];  //补仓浮动
    let sxfArr = [];  //手续费浮动
    let everyBcArr = [];  //每次补仓金额
    let gpslArr = []; //股票数量浮动
    let jczjArr = [];  //补仓资金浮动
    let xzgj = []; //现在股价波动
    let gmsl = 0;
    let insrNum = 0;
    let receNum = 0;
    origMy = ysgj * gpsl   //前一天的持仓金额
    Arithmetic.cssz = origMy  //初始市值
    let three = Math.round(Arithmetic.cssz * 3) / 100
    let six = Math.round(Arithmetic.cssz * 6) / 100
    let nine = Math.round(Arithmetic.cssz * 9) / 100

    let fthree = -Math.round(Arithmetic.cssz * 3) / 100
    let fsix = -Math.round(Arithmetic.cssz * 6) / 100
    let fnine = -Math.round(Arithmetic.cssz * 9) / 100

    let sxfzh = 0;  //手续费总和
    jczj = jczj - Arithmetic.sfjs(true, ysgj * gpsl) + (Arithmetic.csbj - origMy); //现有补仓资金
    let zfjx = Math.round(origMy * zfl) / 100;  //加建仓价格
    let zflj = 0;  //当天浮动资金
    debugger
    for (let i = 0; i <= myArr.length - 1; i++) {
      if (gpsl > 0) {
        // console.log(ysgj);
        zflj += Math.round(origMy * (myArr[i])) / 100
        if (zflj > 0) {
          if(three <= zflj && zflj < six){
             gmsl = 100
          }else if(six <= zflj && zflj < nine){
             gmsl = 200
          }else if(zflj >= nine) {
            gmsl = 300
          }else {
            gmsl = 0
          }
          if(gmsl > 0){
            if (gmsl > gpsl) {
              gmsl = gpsl
            }
            receNum += gmsl
            gpsl = gpsl - Number(gmsl);
            origMy = Math.round(ysgj * gpsl * 100) / 100
            jczj = Math.round((jczj + ysgj * gmsl - Arithmetic.sfjs(true, ysgj * gpsl)) * 100) / 100;  //当天补仓资金结余
            sxf = Arithmetic.sfjs(true, ysgj * gmsl);  //手续费计算
            payOff = ysgj * gmsl//计算当天补仓金额
            zfjx = Math.round(origMy * zfl) / 100;
            zflj = 0
            gmsl = 0
          }
        } else if (zflj < 0) {
          if(fthree >= zflj &&  zflj >= fsix){
            gmsl = 100
          }else if(fsix >= zflj && zflj >= fnine){
            gmsl = 200
          }else if(zflj <= fnine) {
            gmsl = 300
          }else {
            gmsl = 0
          }
          if(gmsl > 0 && Math.round((jczj - ysgj * gmsl - Arithmetic.sfjs(true, ysgj * gpsl)) * 100) / 100 > Arithmetic.cssz / 3){
            insrNum += Math.round((ysgj * gmsl) * 100) / 100
            gpsl = gpsl + Number(gmsl);
            //console.log(gpsl)
            origMy = Math.round((ysgj * gpsl) * 100) / 100
            jczj = Math.round((jczj - ysgj * gmsl - Arithmetic.sfjs(true, ysgj * gpsl)) * 100) / 100;  //当天补仓资金结余
            sxf = Arithmetic.sfjs(false, ysgj * gmsl);  //手续费计算
            payOff = -ysgj * gmsl//计算当天补仓金额
            zfjx = Math.round(origMy *  zfl) / 100;
            zflj = 0
            gmsl = 0
          }
        } else {
          origMy = Math.round(origMy + origMy * myArr[i] / 100)
          payOff = 0;
          sxf = 0;
          three = Math.round(origMy * 3) / 100
          six = Math.round(origMy * 6) / 100
          nine = Math.round(origMy * 9) / 100
        }
      } else {
        break
      }
      payOffArr = Math.round((payOffArr + payOff) * 100) / 100; //补仓浮动
      sxfPay = Math.round((sxfPay + sxf) * 100) / 100; //手续费浮动
      zzc = Math.round((origMy + jczj) * 100) / 100;  //结余总资产
      ccyk = Math.round((zzc - Arithmetic.rszzj) * 100) / 100;  //持仓盈亏
      //console.log(zzc, ccyk)
      sxfzh = Math.round((sxfzh + sxf) * 100) / 100;  //手续费总和
      everyBcArr.push(payOff);  //每次补仓金额
      bcArr.push(payOffArr);  //补仓浮动
      // console.log(ysgj,myArr[i])
      jczjArr.push(jczj);  //补仓资金浮动
      zzcArr.push(zzc)
      sxfArr.push(sxf);
      gpslArr.push(gpsl);
      ysgj = i < myArr.length - 1 ? Math.round((ysgj + Math.round(myArr[i + 1] / 100 * ysgj * 100) / 100) * 100) / 100 : ysgj;  //计算当天价格
      xzgj.push(ysgj);  //现在股价浮动
    }
    console.log(insrNum, receNum)
    incsRo = Math.round(ccyk / (Arithmetic.cssz + insrNum) * 100 * 100) / 100
    successCallback(zzc, jczj, origMy, gpsl, ccyk, incsRo, ysgj, sxfzh, gpslArr, zzcArr, xzgj, everyBcArr, bcArr, jczjArr, sxfArr)
  }
  static gpslInt = (origMy, ysgj) => {
    let gpsl = parseInt(origMy * 100 / parseInt(ysgj * 100)).toString();  //计算当前持有股数
    let len = gpsl.length;  //获取持股数的长度
    gpsl = gpsl > 100 ? Number(gpsl.substr(0, len - 2) + '00') : 100;  //持股数去掉个十位，取百位整数
    return gpsl;
  }
  static sfjs = (bool, sxfPay) => {
    if (!sxfPay) {
      return 0
    } else {
      return bool > 0 ? sxfPay > 10000 ? Math.round(sxfPay * 0.025 / 100 * 100 + sxfPay * 0.1 / 100) / 100 : Math.round(5 + sxfPay * 0.1 / 100) / 100 : sxfPay > 10000 ? Math.round((sxfPay * 0.025 / 100) * 100) / 100 : 5;
    }
  }
  static echartsSvg = (myChart, color, text, xData, series) => {
    let data = series.map(item => {
      return item.name
    })
    let options = {
      color,
      title: {
        text
      },
      tooltip: {
        trigger: 'axis',
      },
      legend: {
        data
      },
      grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true,
      },
      toolbox: {
        feature: {
          saveAsImage: {},
        },
      },
      xAxis: {
        type: 'category',
        boundaryGap: false,
        data: xData,
      },
      yAxis: {
        type: 'value',
        scale: true
      },
      series: series.map((item, index) => {
        return {
          name: data[index],
          type: item.type,
          data: item.data
        }
      })
    }
    myChart.setOption(options)
  }
}
export default Arithmetic

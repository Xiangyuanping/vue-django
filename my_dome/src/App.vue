<template>
  <div id="app">
    <el-container>
      <el-header>交易市场</el-header>
      <el-main>
        <div class="main-c">
          <el-form :inline="true" ref="form" :model="form" label-width="80px">
            <el-form-item label="初始日期">
              <el-date-picker v-model="initTime" type="date" @change="inTime()"/>
            </el-form-item>
            <el-form-item label="涨幅界限">
              <el-input v-model="form.zfl" @change="userlist()"></el-input>
            </el-form-item>
            <el-form-item label="天数">
              <el-select
                v-model="form.day"
                @change="userlist()"
                placeholder="请选择"
              >
                <el-option
                  v-for="item in tssl"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                >
                </el-option>
              </el-select>
            </el-form-item>

            <el-form-item label="持仓本金">
              <el-input v-model="form.origMy"></el-input>
            </el-form-item>
            <el-form-item label="加仓本金">
              <el-input v-model="form.jczj"></el-input>
            </el-form-item>
            <el-form-item label="名称">
              <el-select v-model="form.name" filterable placeholder="请选择" @change="userlist()">
                <el-option
                  v-for="item in gplist"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="时间区间" >
              <el-date-picker
                v-model="form.date"
                @change="userlist()"
                type="daterange"
                range-separator="至"
                start-placeholder="开始日期"
                end-placeholder="结束日期"
              >
              </el-date-picker>
            </el-form-item>
            <el-form-item label="市场选择">
              <el-radio-group v-model="form.resource">
                <el-radio label="0">深证</el-radio>
                <el-radio label="1">上证</el-radio>
              </el-radio-group>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="onSubmit">开始计算</el-button>
            </el-form-item>
          </el-form>
        </div>
        <div class="main-c">
          <el-descriptions title="统计信息">
            <el-descriptions-item label="总资金">{{
              data.zzc
              }}</el-descriptions-item>
            <el-descriptions-item label="补仓本金">{{
              data.jczj
              }}</el-descriptions-item>
            <el-descriptions-item label="持仓市值">{{
              data.origMy
              }}</el-descriptions-item>
            <el-descriptions-item label="持仓股数量">{{
              data.gpsl
              }}</el-descriptions-item>
            <el-descriptions-item label="盈亏额">{{
              data.ccyk
              }}</el-descriptions-item>
            <el-descriptions-item label="盈亏比例"
            >{{ data.incsRo || 0 }}%</el-descriptions-item
            >
            <el-descriptions-item label="收盘股价">{{
              data.ysgj
              }}</el-descriptions-item>
            <el-descriptions-item label="手续费总和">{{
              data.sxfzh
              }}</el-descriptions-item>
            <el-descriptions-item label="现有股价跌幅"
            >{{ gjdf || 0 }}%</el-descriptions-item
            >
            <el-descriptions-item label="多空交量结果"
            >{{ dkjl || 0 }}%</el-descriptions-item
            >
          </el-descriptions>
          <div style="width: 1200px; height: 400px; margin: 30px auto" id="main"></div>
          <div style="width: 1200px; height: 400px; margin: 30px auto" id="jym"></div>
        </div>
      </el-main>
    </el-container>
    <router-view />
  </div>
</template>

<script>
  import Arithmetic from './common/arithmetic'

  export default {
    name: 'index',
    data () {
      return {
        initTime: '2022-03-01',
        gplist: [],
        tssl: [],
        dkjl: 0,  //多空交量结果
        options: [],
        form: {
          day: 30,
          origMy: 19410,
          jczj: 19410,
          name: '美利云',
          date: ['2022-03-17', '2022-04-26'],
          resource: ''
        },
        data: {
          zzc: '', //总资金
          jczj: '', //补仓本金
          origMy: '', //持仓市值
          gpsl: '', //持仓股数量
          ccyk: '', //盈亏额
          incsRo: '', //盈亏比例
          ysgj: '', //收盘股价
          sxfzh: '',  //手续费总和
          gpslArr: [], //股票数量浮动
          zzcArr: [], //总资金浮动
          xzgj: [], //股价浮动
          everyBcArr: [], //补仓金额
          bcArr: [], //补仓浮动
          jczjArr: [], //补仓资金浮动
          sxfArr: [], //手续费浮动

        },
        time: [],
        ueserlist: {},
        yDataArr: [],  //成交量
        gjdf: 0,  //股价跌幅
        zfArr: [],
        timejy: []
      }
    },
    mounted () {
      this.init()
      this.userlist()
    },
    methods: {
      init () {
        const loading = this.$loading({
          lock: true,
          text: '获取所有股票数据中...',
          spinner: 'el-icon-loading',
          background: 'rgba(0, 0, 0, 0.7)'
        });
        let url = 'http://127.0.0.1:8000/app/alllist'
        this.$http.get(url, {}).then((res) => {
          loading.close();
          this.gplist = res.data.data.diff.map(item=>{
            return {
              value: item.f12,
              label: item.f14
            }
          })
        })
        for (let i = 1; i <= 1000; i++) {
          this.tssl.push({
            value: i,
            label: i
          })
          i < 6 ? this.options.push(
            {
              value: i *100,
              label: i* 100 + '股'
            }
          ):''
        }
      },
      inTime(){
        this.form.date = [this.initTime, new Date()]
        this.userlist()
      },
      setDate () {
        let { gpslArr, zzcArr, xzgj, everyBcArr, bcArr, jczjArr, sxfArr } = this.data
        Arithmetic.echartsSvg(this.$echarts.init(document.getElementById('main')),['#40ffc6', 'red', 'pink', 'green', 'blue', 'gray', '#f0ad4e', '#00daff'], '交易系统', this.time,  [
          {
            name: '成交量',
            type: 'bar',
            data: this.yDataArr
          },
          {
            name: '总资金浮动',
            type: 'line',
            data: zzcArr
          },
          {
            name: '价格浮动',
            type: 'line',
            data: xzgj
          },
          {
            name: '数量浮动',
            type: 'line',
            data: gpslArr
          },
          {
            name: '补仓金额',
            type: 'line',
            data: everyBcArr
          },
          {
            name: '补仓浮动',
            type: 'line',
            data: bcArr
          },
          {
            name: '补仓资金浮动',
            type: 'line',
            data: jczjArr
          },
          {
            name: '手续费浮动',
            type: 'line',
            data: sxfArr
          }
        ])
        Arithmetic.echartsSvg(this.$echarts.init(document.getElementById('jym')),['#a71894'], '交易系统', this.timejy, [
          {
            name: '最佳买入点',
            type: 'line',
            data: this.zfArr,
          }
        ])
      },
      userlist () {
         this.form.day = parseInt(new Date(this.form.date[0]).getTime() /24 /60 /60/1000) - parseInt(new Date(this.initTime).getTime() /24 /60 /60/1000)
        // this.form.date = [this.initTime, new Date()]
         //this.initTime ? this.form.day = this.form.day + (parseInt(new Date(this.form.date[0]).getTime() /24 /60 /60/1000) - parseInt(new Date(this.initTime).getTime() /24 /60 /60/1000)) : ''
        const loading = this.$loading({
          lock: true,
          text: '获取' + this.form.name + '股票信息中...',
          spinner: 'el-icon-loading',
          background: 'rgba(0, 0, 0, 0.7)'
        });
        let url = 'http://127.0.0.1:8000/app/userlist?name=' + this.form.name;
        this.$http.get(url, {}).then((res) => {
          loading.close();
          let value = res.data.QuotationCodeTable.Data[0]
          this.ueserlist = value;
          this.form.resource = value.MktNum
          this.onSubmit()
        })
      },
      onSubmit () {
        this.time = [];
        const loading1 = this.$loading({
          lock: true,
          text:  '获取' + this.form.name + '股票历年信息中...',
          spinner: 'el-icon-loading',
          background: 'rgba(0, 0, 0, 0.7)'
        });
        this.yDataArr = [];
        let nValue = [];
        let myArr = [];
        this.zfArr = [];
        this.timejy = []
        let ysgj = 0;
        let eight = 8 * 60 * 60 * 1000
        let sjq = new Date(this.form.date[0]).getTime() + eight
        let sjz = new Date(this.form.date[1]).getTime() + eight
        let zxValue = []
        let jgsj = Number(this.form.day) * 24 * 60 * 60 * 1000
        const url = 'http://127.0.0.1:8000/app/request?name=' + this.ueserlist.Code + '&type=' + this.form.resource
        this.$http.get(url).then((res) => {
          loading1.close()
          let value = res.data.data.klines
          value = value.map(item => {
            return item.split(',');
          })
          for (let i = 0; i <= value.length - 1; i++) {
            if (sjq - jgsj <= new Date(value[i][0]).getTime() && sjz >= new Date(value[i][0]).getTime()) {
              nValue.push(value[i]);
              this.timejy.push(value[i][0]);
            }
          }
          let yDataArr = [];
          let zfh = 0;
          let z = 0;
          let pjl = 0
          let u = 0;
           console.log(nValue);
          // console.log(this.timejy)
          for (let w = 0; w <= nValue.length - 1; w++) {
            let kstime = new Date(nValue[w][0]).getTime()
            if (sjq - jgsj <= kstime && sjq > kstime) {
              //console.log(w)
              zfh = Math.abs(Math.round(Number(nValue[w][8]) * 100) / 100)
              z += Math.round(Number(nValue[w][8]) * 100) / 100
              this.zfArr.push(Math.round(z * 100) / 100)
              u++
            } else {
              this.time.push(nValue[w][0])
              zxValue.push(nValue[w]);
            }
          }
          // console.log(new Date(nValue[nValue.length - 1][0]).getTime() === sjq)
          // if(new Date(nValue[nValue.length - 1][0]).getTime() === sjq){
          //   this.time.push(nValue[nValue.length - 1][0])
          //   zxValue.push(nValue[nValue.length - 1]);
          //   this.gjdf = zxValue[0][2]
          // }
          this.gjdf = Math.round(((Number(nValue[nValue.length - 1][2]) - Number(nValue[u - 1][2])) / Number(nValue[u - 1][2])) * 100 * 100) / 100;
          this.dkjl = Math.round(z * 100) / 100;
          //console.log(zxValue)
          if (zxValue.length > 0) {
            ysgj = Number(zxValue[0][2]);
            for (let j = 0; j <= zxValue.length - 1; j++) {
              myArr.push(Number(zxValue[j][8]));
              yDataArr.push(Math.round(zxValue[j][5]));
            }
            this.yDataArr = yDataArr;

            console.log(nValue.length - zxValue.length, zfh);
            pjl = nValue.length - zxValue.length;
            let zfje = Math.round(zfh / pjl * 100) / 100
            //this.form.zfl = 6
            let bj = ysgj * 1000;
            Arithmetic.getData(this.form.zfl, Number(this.form.origMy), Number(this.form.jczj), 1, myArr, ysgj, (zzc, jczj, origMy, gpsl, ccyk, incsRo, ysgj, sxfzh, gpslArr, zzcArr, xzgj, everyBcArr, bcArr, jczjArr, sxfArr) => {
                let arr = [zzc, jczj, origMy, gpsl, ccyk, incsRo, ysgj, sxfzh, gpslArr, zzcArr, xzgj, everyBcArr, bcArr, jczjArr, sxfArr]
                let i = 0
                for (const key in this.data) {
                  this.data[key] = arr[i]
                  i++
                }
                this.setDate()
              }
            )
          }

        })
      }
    },
  }
</script>

<style scoped>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    width: 1600px;
    margin: 0 auto;
  }
  .main-c {
    width: 1200px;
    margin: 0 auto;
  }
  table tr td {
    border: 1px solid red;
  }
</style>

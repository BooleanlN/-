<template>
 <div class="login-container">
   <div class="title">现场计量设备
     <span>运行风险预测与评价软件</span>
   </div>
    <div class="box-wrapper">
      <div class="registe-box">
        <div class="registe">
          <div class="box-title">
            <h1>注&nbsp;&nbsp;&nbsp;&nbsp;册</h1>
          </div>
          <el-input v-model="userConfig.username" placeholder="输入账号名"></el-input>
          <el-input v-model="userConfig.password" placeholder="输入密码" show-password></el-input>
          <el-input v-model="passwordAgain" placeholder="请再次输入密码" show-password></el-input>
          <el-input v-model="userConfig.email" placeholder="请输入电子邮箱" type="email"></el-input>
          <el-button type="primary" style="margin-top:10px;" @click="registe" class="btnbgcolor">注册</el-button>
          <el-button type="primary" style="margin-top:10px;" @click="tologin" class="btnbgcolor">去登录</el-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */ 
import userApi from '@/Api/user-operation'
export default {
  data() {
    return {
     userConfig:{
        username: '',
        password: ''
     },
     passwordAgain: ''
    }
  },
  created () {},
  methods: {
    registe () {
      if(this.userConfig.username == '' || this.userConfig.password == ''){
        this.$message.error('账号密码不能为空')
        return
      }else if(this.passwordAgain !== this.userConfig.password){
        this.$message.error('两次输入密码不一致')
        return
      }
      let formData = new FormData()
      formData.append('username', this.userConfig.username)
      formData.append('password', this.userConfig.password)
      userApi.userRegiste(formData).then(response => {
        this.$message.success('注册成功')
        this.$router.push({
          name: "main",
        });
      }).catch(error => {
        this.$message.error('注册失败')
      })
    },
    tologin () {
      this.$router.push({
        path:'/login'
      })
    }
  }
};
</script>

<style lang="scss" scope>
@import "../assets/style.scss";
.login-container {
  position: fixed;
  width: 100%;
  height: 100%;
  background: #545c64;
  .title{
    font-family: 'BebasNeueRegular', 'Arial Narrow', Arial, sans-serif;
    font-size: 35px;
    line-height: 35px;
    position: relative;
    font-weight: 400;
    color: rgba(255,255,255,0.9);
    text-shadow: 1px 1px 1px rgba(0,0,0,0.1);
    padding: 80px 0px 5px 0px;
    text-align: center;
    width: 100%;
    span{
      color: #7cbcd6;
      text-shadow: 0px 1px 1px rgba(0,124,119,0.8);
    }
  }
  .box-wrapper {
    width: 100%;
    position: relative;
    height: 300px;
    .login-box {
      width: 500px;
      height: 350px;
      background: #fff;
      // margin: auto;
      position: absolute;
      top: 20%;
      left: 35%;
      border-radius: 10px;
      .login {
        margin: 70px;
        .box-title{
          text-align: center;
          h1{
            color: #007A77;
          }
        }
        .el-input {
          margin-top: 20px;
        }
      }
    }
    .registe-box{
      width: 500px;
      height: 500px;
      background: #fff;
      position: absolute;
      top: 20%;
      left: 35%;
      border-radius: 10px;
      .registe{
        margin: 70px;
        .box-title{
          text-align: center;
          h1{
            color: #007A77;
          }
        }
        .el-input {
          margin-top: 20px;
        }
      }
    }
  }
}
</style>

<template>
  <div class="tagTree">
    <button @click="backward">Back</button>
    <ul v-for="tag in tagList">
      <li @click="nextTag(tag)">{{ tag }}</li>
    </ul>
    {{direc}}
  </div>

</template>

<script>
  export default {
    name: 'tagTree',
    data () {
      return {
        tagList: [
        ],
        direc: 'cs.ai',
        userId: "10032",
        getFail: false,
      }
    },
    methods: {
      backward: function () {
        var oriDir = String(this.direc)
        if (!this.direc || this.direc.length == 0) {
          alert("Error: path is empty!");
        } else {
          var itemList = oriDir.split('.');
          console.log('Oridir ' + oriDir);
          console.log(' and spl: ' + oriDir.split('.'))
          console.log('Item List is: ' + itemList.length)
          if (itemList.length == 1) {
            alert("Error: this is root dir!");
          }
          else if (!itemList) {
            alert("Error: no itemList. Current directory is: " + oriDir)
          }
          else {
            var newDir = ''
            for (var i = 0; i < itemList.length - 1; i++) {
              if (i == 0) {
                newDir = newDir + itemList[i]
              } else {
                newDir = newDir + '.' + itemList[i]
              }
            }
            this.direc = newDir
            this.showTags()
            if (this.getFail) {
              this.direc = oriDir
              this.getFail = false
            }
          }
        }
      },
      nextTag: function (tag) {
        var oriDir = String(this.direc)
        console.log('Origin dir: ' + this.direc)
        if (!this.direc || this.direc.length == 0) {
          this.direc = String(tag)
        } else {
          this.direc = this.direc + '.' + String(tag)
        }
        this.showTags()
        console.log(this.getFail)
        console.log('Before show: ' + this.direc)
        if (this.getFail == true) {
          this.direc = oriDir
          this.getFail = false
          console.log('direc: ' + this.direc + ' and ori: ' + oriDir)
        }
        console.log('After show: ' + this.direc)
      },
      showTags () {
        res = this.$http.get('http://127.0.0.1:8080/api/getTagList?userId=' + this.userId + '&currentPath=' + this.direc)
          .then((response) => {
            var res = JSON.parse(response.bodyText)
            if (res['error_num'] == 0) {
              this.tagList = res['tagList']
            } else {
              this.$message.error('Error: cannot get tag list!')
              console.log(res['msg'])
              this.getFail = true
            }
          })
      },
    },
    mounted: function() {
      //这个是钩子函数
      //如果cartView函数要执行，必须先执行钩子函数
      //这个钩子函数完成了对cratView函数的调用
      //应该注意的是，使用mounted 并不能保证钩子函数中的 this.$el 在 document 中。为此还应该引入             Vue.nextTick/vm.$nextTick
      this.$nextTick(function () {
        this.showTags()
      })
    }
  }
</script>

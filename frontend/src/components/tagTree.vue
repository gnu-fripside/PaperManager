<template>
  <div>
    <button @click="backward">Back</button>
    <ul v-for="tag in tagList">
      <li @click="nextTag(tag)">{{ tag }}</li>
    </ul>
  </div>

</template>

<script>
  export default {
    name: 'tagTree',
    data () {
      return {
        tagList: [
          'a',
          'b',
          'c',
        ],
        direc: '',
        getFail: false,
      }
    },
    methods: {
      backward: function () {
        var oriDir = String(this.direc)
        if (!this.direc || this.direc.length == 0) {
          alert("Error: path is empty!");
        } else {
          itemList = this.direc.split('.');
          if (itemList.length == 1) {
            alert("Error: this is root dir!");
          } else {
            newDir = '';
            for (var i = 0; i < itemList.length - 1; i++) {
              if (i == 0) {
                newDir = newDir + itemList[i];
              } else {
                newDir = newDir + '.' + itemList[i];
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
        res = this.$http.get('http://127.0.0.1:8080/api/getTagList?currentPath=' + this.direc)
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
    }
  }
</script>

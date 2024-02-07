<template>
    <div class="container">
      <div class="row">
        <div class="d-flex justify-content-between align-items-center">
          <span class="text-left item-size">{{ item.name }}</span>
          <div class="d-flex">
            <i class="fa-solid fa-file-lines icon-size icon-spacing"></i>            
            <i class="fa-regular fa-rectangle-xmark icon-size icon-spacing" style="color: #511f1f;"></i>
          </div>
        </div>
      </div>
    </div>
</template>

<script lang>
export default {
    props:{
        item: {
            type:Object,
            required:true
        }
    }
}
</script>

<style scoped>
.item-size{
    font-size: 20px
}

.icon-size{
    font-size: 20px;
}

.row{
  padding-top: 5px;
}

.icon-spacing{
    margin-right: 5px;
    margin-left: 5px;
}
</style>
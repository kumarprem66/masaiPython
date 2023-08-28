import { Component, OnInit } from '@angular/core';
import { Post } from '../data-type';

@Component({
  selector: 'app-post',
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.css']
})
export class PostComponent implements OnInit{

  
  postList:Post[] = []
  ngOnInit(): void {
    
  }

  posting(data:Post){
    
    data.id = Math.floor((Math.random()+1)*10)
    this.postList.push(data)
    console.log(data)

  }

  showpostList():any{
    
    this.postList.forEach((element:any) => {
      console.log(element)
    });

    console.log(this.postList.length)
  }


  delete(id:any){

    let intorem  = this.postList.findIndex(ob => ob.id == id);

    if(intorem !== -1){
      this.postList.splice(intorem,1)
    }
   
    console.log(this.postList)
  }

}

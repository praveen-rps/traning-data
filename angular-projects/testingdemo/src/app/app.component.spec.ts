import { ComponentFixture, TestBed } from '@angular/core/testing';
import { AppComponent } from './app.component';


describe('GreetingComponent', ()=>{
  let component : AppComponent;
  let fixture : ComponentFixture<AppComponent>;

  beforeEach(()=>{
    TestBed.configureTestingModule({
      declarations :[AppComponent]
    }).compileComponents();
    fixture = TestBed.createComponent(AppComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();

  });

  it('should return the msssage', ()=>{
    const result = component.greeting('Anil');
    expect(result).toEqual("Hello Anil Welcome to Angular Testing")
  });

});  


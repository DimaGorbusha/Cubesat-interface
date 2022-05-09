import React from "react";
import "../Styles/SignUp.css";
import { Form, Button } from 'bootstrap-4-react';

export const SignUp = () => {
    return (
        <div className="content">
            <div className="container_sign">
                <h2 style={{fontFamily:'Montserrat-Bold', marginBottom:'20px'}}>Вход</h2>
                <Form.Group>
                    <Form.Input style={{width:'-webkit-fill-available',fontFamily:'Montserrat-Regular', borderRadius:'10px', padding: '15px'}} type="password" placeholder="Пароль" shadow />
                    {/* <Form.Text text="muted">или войдите через режим гостя</Form.Text> */}
                </Form.Group>
                <Button id="btn_sign" className="btn_sign" class="btn_sign" style={{width:'-webkit-fill-available', borderRadius:'20px', fontFamily:'Montserrat-Medium', backgroundColor:'#FF4D00', borderColor:'white', outline:'none'}} primary as="input" type="button" value="Войти" />
                <p style={{marginTop:'10px'}}>Войти как гость</p>
            </div>
        </div>
    )
}
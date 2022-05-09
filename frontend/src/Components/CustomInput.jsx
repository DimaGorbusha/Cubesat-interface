import React from "react";
import { Form, Button } from 'bootstrap-4-react';

export const CustomInput = ({label, placeholder, type}) => {
    return (
        <Form.Group style={{marginRight:'20px', marginBottom:'20px'}}>
            <label htmlFor="exampleInputEmail1">{label}</label>
            <Form.Input style={{ width: 'fit-content', fontFamily: 'Montserrat-Regular', borderRadius: '10px', padding: '15px' }} type={type} placeholder={placeholder} shadow />
            {/* <Form.Text text="muted">или войдите через режим гостя</Form.Text> */}
        </Form.Group>
    )
}
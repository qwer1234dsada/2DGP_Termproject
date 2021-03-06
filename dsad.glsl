#version 330
//--- in_Position: attribute index 0
//--- in_Color: attribute index 1
layout(location = 0) in vec3 in_Position;//--- 위치 속성
in vec3 in_Color; //--- 색상 속성
out vec3 ex_Color; // 프래그먼트 세이더에게 전달

uniform mat4 transform;
uniform mat4 viewport;
uniform mat4 projectionTransform;
uniform vec3 uniformColor;

void main(void)
{
gl_Position = projectionTransform*viewport*transform*vec4 (in_Position.x, in_Position.y, in_Position.z, 1.0);
ex_Color = uniformColor;
}
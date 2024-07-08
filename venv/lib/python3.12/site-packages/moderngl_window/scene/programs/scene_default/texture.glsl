#version 330

#if defined VERTEX_SHADER

in vec3 in_position;
in vec2 in_texcoord_0;

uniform mat4 m_proj;
uniform mat4 m_model;
uniform mat4 m_cam;

out vec2 uv;

void main() {
	gl_Position = m_proj * m_cam * m_model * vec4(in_position, 1.0);
    uv = in_texcoord_0;
}

#elif defined FRAGMENT_SHADER

out vec4 fragColor;
uniform sampler2D texture0;

in vec2 uv;

void main()
{
    fragColor = texture(texture0, uv);
}

#endif

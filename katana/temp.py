def psnProcedural(nodeName = 'Default'):
    xmlTree =f'''<katana release="3.1v5" version="3.1.3.000001">
  <node name="__SAVE_exportedNodes" type="Group">
    <node baseType="NetworkMaterial" name="{nodeName}_NetworkMaterial" selected="true" type="NetworkMaterial" x="295.000000" y="146.500000">
      <port name="prmanBxdf" source="{nodeName}_PSN.out" type="in">
        <tags>
          <tag name="bxdf"/>
        </tags>
      </port>
      <port name="out" type="out"/>
      <group_parameter name="{nodeName}_NetworkMaterial">
        <string_parameter name="name" value="{nodeName}_NetworkMaterial"/>
        <string_parameter name="namespace" value=""/>
        <string_parameter name="addTerminal" value=""/>
        <stringarray_parameter name="publicInterfaceOrder" size="0" tupleSize="1"/>
      </group_parameter>
    </node>
    <node baseType="PrmanShadingNode" name="{nodeName}_dirt" selected="true" type="PrmanShadingNode" x="301.000000" y="284.500000">
      <port name="occluded" type="in">
        <metadata>
          <entry key="page" value="Dirt Color"/>
          <entry key="label" value="Occluded"/>
        </metadata>
      </port>
      <port name="unoccluded" type="in">
        <metadata>
          <entry key="page" value="Dirt Color"/>
          <entry key="label" value="Unoccluded"/>
        </metadata>
      </port>
      <port name="biasDirection" type="in">
        <metadata>
          <entry key="page" value="Sampling"/>
          <entry key="label" value="Bias Direction"/>
        </metadata>
      </port>
      <port name="traceSet" type="in">
        <metadata>
          <entry key="page" value="Sampling"/>
          <entry key="label" value="Trace Set"/>
        </metadata>
      </port>
      <port name="resultRGB" type="out">
        <tags>
          <tag name="color"/>
          <tag name="normal"/>
          <tag name="point"/>
          <tag name="vector"/>
        </tags>
      </port>
      <port name="resultR" type="out">
        <tags>
          <tag name="float"/>
        </tags>
      </port>
      <port name="resultG" type="out">
        <tags>
          <tag name="float"/>
        </tags>
      </port>
      <port name="resultB" type="out">
        <tags>
          <tag name="float"/>
        </tags>
      </port>
      <group_parameter name="{nodeName}_dirt">
        <string_parameter name="name" value="{nodeName}_dirt"/>
        <string_parameter name="nodeType" value="PxrDirt"/>
        <string_parameter name="__lastValue" value="4hjav6csvrphjzo4l6ukmexafq7bf6wwvecg3hj3xttb3sz6wegqFalse"/>
        <string_parameter name="__showHiddenParams" value="False"/>
        <group_parameter name="parameters">
          <group_parameter name="occluded">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="1"/>
              <number_parameter name="i1" value="1"/>
              <number_parameter name="i2" value="1"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="unoccluded">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="numSamples">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="4"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="distribution">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="1"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="cosineSpread">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="1"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="falloff">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="maxDistance">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="direction">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="biasDirection">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="biasDirectionCoordsys">
            <number_parameter name="enable" value="0"/>
            <string_parameter name="value" value="object"/>
            <string_parameter name="type" value="StringAttr"/>
          </group_parameter>
          <group_parameter name="traceSet">
            <number_parameter name="enable" value="0"/>
            <string_parameter name="value" value=""/>
            <string_parameter name="type" value="StringAttr"/>
          </group_parameter>
          <group_parameter name="__unused"/>
        </group_parameter>
        <group_parameter name="publicInterface">
          <string_parameter name="namePrefix" value=""/>
          <string_parameter name="pagePrefix" value=""/>
          <string_parameter name="nameRegExFind" value=""/>
          <string_parameter name="nameRegExReplace" value=""/>
          <string_parameter name="pageRegExFind" value=""/>
          <string_parameter name="pageRegExReplace" value=""/>
        </group_parameter>
        <string_parameter name="forceRefresh" value=""/>
      </group_parameter>
    </node>
    <node baseType="PrmanShadingNode" edited="true" name="{nodeName}_blend" selected="true" type="PrmanShadingNode" x="301.000000" y="240.500000">
      <port name="topRGB" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="label" value="Top Color"/>
        </metadata>
      </port>
      <port name="topA" source="{nodeName}_dirt.resultR" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="label" value="Top Alpha"/>
        </metadata>
      </port>
      <port name="bottomRGB" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="label" value="Bottom Color"/>
        </metadata>
      </port>
      <port name="bottomA" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="label" value="Bottom Alpha"/>
        </metadata>
      </port>
      <port name="resultRGB" type="out">
        <tags>
          <tag name="color"/>
          <tag name="normal"/>
          <tag name="point"/>
          <tag name="vector"/>
        </tags>
      </port>
      <port name="resultR" type="out">
        <tags>
          <tag name="float"/>
        </tags>
      </port>
      <port name="resultG" type="out">
        <tags>
          <tag name="float"/>
        </tags>
      </port>
      <port name="resultB" type="out">
        <tags>
          <tag name="float"/>
        </tags>
      </port>
      <port name="resultA" type="out">
        <tags>
          <tag name="float"/>
        </tags>
      </port>
      <group_parameter name="{nodeName}_blend">
        <string_parameter name="name" value="{nodeName}_blend"/>
        <string_parameter name="nodeType" value="PxrBlend"/>
        <string_parameter name="__lastValue" value="bzea23qggbox46gf3kte7o54wegkqmq5yvosayzzeqp6rkx5hl64False"/>
        <string_parameter name="__showHiddenParams" value="False"/>
        <group_parameter name="parameters">
          <group_parameter name="operation">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="19"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="topRGB">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="topA">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="1"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="bottomRGB">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="bottomA">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="1"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="clampOutput">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="1"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="__unused"/>
        </group_parameter>
        <group_parameter name="publicInterface">
          <string_parameter name="namePrefix" value=""/>
          <string_parameter name="pagePrefix" value=""/>
          <string_parameter name="nameRegExFind" value=""/>
          <string_parameter name="nameRegExReplace" value=""/>
          <string_parameter name="pageRegExFind" value=""/>
          <string_parameter name="pageRegExReplace" value=""/>
        </group_parameter>
        <string_parameter name="forceRefresh" value=""/>
      </group_parameter>
    </node>
    <node baseType="PrmanShadingNode" name="{nodeName}_PSN" selected="true" type="PrmanShadingNode" x="295.000000" y="193.500000">
      <port name="inputMaterial" type="in">
        <tags>
          <tag name="vstruct"/>
        </tags>
        <metadata>
          <entry key="label" value="Input Material"/>
        </metadata>
      </port>
      <port name="diffuseGain" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Diffuse"/>
          <entry key="label" value="Gain"/>
        </metadata>
      </port>
      <port name="diffuseColor" source="{nodeName}_blend.resultRGB" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="page" value="Diffuse"/>
          <entry key="label" value="Color"/>
        </metadata>
      </port>
      <port name="diffuseRoughness" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Diffuse"/>
          <entry key="label" value="Roughness"/>
        </metadata>
      </port>
      <port name="diffuseExponent" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Diffuse.Advanced"/>
          <entry key="label" value="Exponent"/>
        </metadata>
      </port>
      <port name="diffuseBumpNormal" type="in">
        <tags>
          <tag name="normal"/>
        </tags>
        <metadata>
          <entry key="page" value="Diffuse.Advanced"/>
          <entry key="label" value="Bump"/>
        </metadata>
      </port>
      <port name="diffuseBackColor" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="page" value="Diffuse.Advanced"/>
          <entry key="label" value="Back Color"/>
        </metadata>
      </port>
      <port name="diffuseTransmitGain" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Diffuse.Advanced"/>
          <entry key="label" value="Transmit Gain"/>
        </metadata>
      </port>
      <port name="diffuseTransmitColor" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="page" value="Diffuse.Advanced"/>
          <entry key="label" value="Transmit Color"/>
        </metadata>
      </port>
      <port name="specularFaceColor" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="page" value="Primary Specular"/>
          <entry key="label" value="Face Color"/>
        </metadata>
      </port>
      <port name="specularEdgeColor" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="page" value="Primary Specular"/>
          <entry key="label" value="Edge Color"/>
        </metadata>
      </port>
      <port name="specularFresnelShape" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Primary Specular"/>
          <entry key="label" value="Fresnel Exponent"/>
        </metadata>
      </port>
      <port name="specularIor" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="page" value="Primary Specular"/>
          <entry key="label" value="Refraction Index"/>
        </metadata>
      </port>
      <port name="specularExtinctionCoeff" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="page" value="Primary Specular"/>
          <entry key="label" value="Extinction Coefficient"/>
        </metadata>
      </port>
      <port name="specularRoughness" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Primary Specular"/>
          <entry key="label" value="Roughness"/>
        </metadata>
      </port>
      <port name="specularAnisotropy" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Primary Specular.Advanced"/>
          <entry key="label" value="Anisotropy"/>
        </metadata>
      </port>
      <port name="specularAnisotropyDirection" type="in">
        <tags>
          <tag name="vector"/>
        </tags>
        <metadata>
          <entry key="page" value="Primary Specular.Advanced"/>
          <entry key="label" value="Shading Tangent"/>
        </metadata>
      </port>
      <port name="specularBumpNormal" type="in">
        <tags>
          <tag name="normal"/>
        </tags>
        <metadata>
          <entry key="page" value="Primary Specular.Advanced"/>
          <entry key="label" value="Bump"/>
        </metadata>
      </port>
      <port name="roughSpecularFaceColor" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="page" value="Rough Specular"/>
          <entry key="label" value="Face Color"/>
        </metadata>
      </port>
      <port name="roughSpecularEdgeColor" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="page" value="Rough Specular"/>
          <entry key="label" value="Edge Color"/>
        </metadata>
      </port>
      <port name="roughSpecularFresnelShape" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Rough Specular"/>
          <entry key="label" value="Fresnel Exponent"/>
        </metadata>
      </port>
      <port name="roughSpecularIor" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="page" value="Rough Specular"/>
          <entry key="label" value="Refraction Index"/>
        </metadata>
      </port>
      <port name="roughSpecularExtinctionCoeff" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="page" value="Rough Specular"/>
          <entry key="label" value="Extinction Coefficient"/>
        </metadata>
      </port>
      <port name="roughSpecularRoughness" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Rough Specular"/>
          <entry key="label" value="Roughness"/>
        </metadata>
      </port>
      <port name="roughSpecularAnisotropy" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Rough Specular.Advanced"/>
          <entry key="label" value="Anisotropy"/>
        </metadata>
      </port>
      <port name="roughSpecularAnisotropyDirection" type="in">
        <tags>
          <tag name="vector"/>
        </tags>
        <metadata>
          <entry key="page" value="Rough Specular.Advanced"/>
          <entry key="label" value="Shading Tangent"/>
        </metadata>
      </port>
      <port name="roughSpecularBumpNormal" type="in">
        <tags>
          <tag name="normal"/>
        </tags>
        <metadata>
          <entry key="page" value="Rough Specular.Advanced"/>
          <entry key="label" value="Bump"/>
        </metadata>
      </port>
      <port name="clearcoatFaceColor" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="page" value="Clear Coat"/>
          <entry key="label" value="Face Color"/>
        </metadata>
      </port>
      <port name="clearcoatEdgeColor" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="page" value="Clear Coat"/>
          <entry key="label" value="Edge Color"/>
        </metadata>
      </port>
      <port name="clearcoatFresnelShape" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Clear Coat"/>
          <entry key="label" value="Fresnel Exponent"/>
        </metadata>
      </port>
      <port name="clearcoatIor" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="page" value="Clear Coat"/>
          <entry key="label" value="Refraction Index"/>
        </metadata>
      </port>
      <port name="clearcoatExtinctionCoeff" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="page" value="Clear Coat"/>
          <entry key="label" value="Extinction Coefficient"/>
        </metadata>
      </port>
      <port name="clearcoatThickness" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Clear Coat"/>
          <entry key="label" value="Layer Thickness"/>
        </metadata>
      </port>
      <port name="clearcoatAbsorptionTint" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="page" value="Clear Coat"/>
          <entry key="label" value="Absorption Tint"/>
        </metadata>
      </port>
      <port name="clearcoatRoughness" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Clear Coat"/>
          <entry key="label" value="Roughness"/>
        </metadata>
      </port>
      <port name="clearcoatAnisotropy" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Clear Coat.Advanced"/>
          <entry key="label" value="Anisotropy"/>
        </metadata>
      </port>
      <port name="clearcoatAnisotropyDirection" type="in">
        <tags>
          <tag name="vector"/>
        </tags>
        <metadata>
          <entry key="page" value="Clear Coat.Advanced"/>
          <entry key="label" value="Shading Tangent"/>
        </metadata>
      </port>
      <port name="clearcoatBumpNormal" type="in">
        <tags>
          <tag name="normal"/>
        </tags>
        <metadata>
          <entry key="page" value="Clear Coat.Advanced"/>
          <entry key="label" value="Bump"/>
        </metadata>
      </port>
      <port name="iridescenceFaceGain" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Iridescence"/>
          <entry key="label" value="Face gain"/>
        </metadata>
      </port>
      <port name="iridescenceEdgeGain" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Iridescence"/>
          <entry key="label" value="Edge gain"/>
        </metadata>
      </port>
      <port name="iridescenceFresnelShape" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Iridescence"/>
          <entry key="label" value="Fresnel Exponent"/>
        </metadata>
      </port>
      <port name="iridescencePrimaryColor" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="page" value="Iridescence"/>
          <entry key="label" value="Primary Color"/>
        </metadata>
      </port>
      <port name="iridescenceSecondaryColor" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="page" value="Iridescence"/>
          <entry key="label" value="Secondary Color"/>
        </metadata>
      </port>
      <port name="iridescenceRoughness" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Iridescence"/>
          <entry key="label" value="Roughness"/>
        </metadata>
      </port>
      <port name="iridescenceAnisotropy" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Iridescence.Advanced"/>
          <entry key="label" value="Anisotropy"/>
        </metadata>
      </port>
      <port name="iridescenceAnisotropyDirection" type="in">
        <tags>
          <tag name="vector"/>
        </tags>
        <metadata>
          <entry key="page" value="Iridescence.Advanced"/>
          <entry key="label" value="Shading Tangent"/>
        </metadata>
      </port>
      <port name="iridescenceBumpNormal" type="in">
        <tags>
          <tag name="normal"/>
        </tags>
        <metadata>
          <entry key="page" value="Iridescence.Advanced"/>
          <entry key="label" value="Bump"/>
        </metadata>
      </port>
      <port name="iridescenceCurve" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Iridescence.Advanced"/>
          <entry key="label" value="Falloff Speed"/>
        </metadata>
      </port>
      <port name="iridescenceScale" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Iridescence.Advanced"/>
          <entry key="label" value="Falloff Scale"/>
        </metadata>
      </port>
      <port name="iridescenceThickness" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Iridescence.Advanced"/>
          <entry key="label" value="Thin Film Thickness"/>
        </metadata>
      </port>
      <port name="fuzzGain" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Fuzz"/>
          <entry key="label" value="Gain"/>
        </metadata>
      </port>
      <port name="fuzzColor" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="page" value="Fuzz"/>
          <entry key="label" value="Color"/>
        </metadata>
      </port>
      <port name="fuzzConeAngle" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Fuzz"/>
          <entry key="label" value="Cone Angle"/>
        </metadata>
      </port>
      <port name="fuzzBumpNormal" type="in">
        <tags>
          <tag name="normal"/>
        </tags>
        <metadata>
          <entry key="page" value="Fuzz.Advanced"/>
          <entry key="label" value="Bump"/>
        </metadata>
      </port>
      <port name="subsurfaceGain" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Subsurface"/>
          <entry key="label" value="Gain"/>
        </metadata>
      </port>
      <port name="subsurfaceColor" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="page" value="Subsurface"/>
          <entry key="label" value="Color"/>
        </metadata>
      </port>
      <port name="subsurfaceDmfp" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Subsurface"/>
          <entry key="label" value="Mean Free Path Distance"/>
        </metadata>
      </port>
      <port name="subsurfaceDmfpColor" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="page" value="Subsurface"/>
          <entry key="label" value="Mean Free Path Color"/>
        </metadata>
      </port>
      <port name="shortSubsurfaceGain" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Subsurface"/>
          <entry key="label" value="Short Gain"/>
        </metadata>
      </port>
      <port name="shortSubsurfaceColor" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="page" value="Subsurface"/>
          <entry key="label" value="Short Color"/>
        </metadata>
      </port>
      <port name="shortSubsurfaceDmfp" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Subsurface"/>
          <entry key="label" value="Short MFP Distance"/>
        </metadata>
      </port>
      <port name="longSubsurfaceGain" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Subsurface"/>
          <entry key="label" value="Long Gain"/>
        </metadata>
      </port>
      <port name="longSubsurfaceColor" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="page" value="Subsurface"/>
          <entry key="label" value="Long Color"/>
        </metadata>
      </port>
      <port name="longSubsurfaceDmfp" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Subsurface"/>
          <entry key="label" value="Long MFP Distance"/>
        </metadata>
      </port>
      <port name="subsurfaceDirectionality" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Subsurface"/>
          <entry key="label" value="Directionality"/>
        </metadata>
      </port>
      <port name="subsurfaceBleed" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Subsurface"/>
          <entry key="label" value="Bleed"/>
        </metadata>
      </port>
      <port name="subsurfaceDiffuseBlend" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Subsurface"/>
          <entry key="label" value="Diffuse Blend"/>
        </metadata>
      </port>
      <port name="subsurfacePostTint" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="page" value="Subsurface.Advanced"/>
          <entry key="label" value="Post Tint"/>
        </metadata>
      </port>
      <port name="subsurfaceTransmitGain" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Subsurface.Advanced"/>
          <entry key="label" value="Transmit Gain"/>
        </metadata>
      </port>
      <port name="singlescatterGain" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Single Scatter"/>
          <entry key="label" value="Gain"/>
        </metadata>
      </port>
      <port name="singlescatterColor" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="page" value="Single Scatter"/>
          <entry key="label" value="Color"/>
        </metadata>
      </port>
      <port name="singlescatterMfp" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Single Scatter"/>
          <entry key="label" value="Mean Free Path"/>
        </metadata>
      </port>
      <port name="singlescatterMfpColor" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="page" value="Single Scatter"/>
          <entry key="label" value="Mean Free Path Color"/>
        </metadata>
      </port>
      <port name="singlescatterDirectionality" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Single Scatter.Advanced"/>
          <entry key="label" value="Directionality"/>
        </metadata>
      </port>
      <port name="singlescatterIor" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Single Scatter.Advanced"/>
          <entry key="label" value="Refractive Index"/>
        </metadata>
      </port>
      <port name="singlescatterBlur" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Single Scatter.Advanced"/>
          <entry key="label" value="Blur"/>
        </metadata>
      </port>
      <port name="singlescatterDirectGain" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Single Scatter.Advanced"/>
          <entry key="label" value="Backside Direct Gain"/>
        </metadata>
      </port>
      <port name="singlescatterDirectGainTint" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="page" value="Single Scatter.Advanced"/>
          <entry key="label" value="Direct Gain Tint"/>
        </metadata>
      </port>
      <port name="irradianceTint" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="page" value="Scattering Globals"/>
          <entry key="label" value="Irradiance Tint"/>
        </metadata>
      </port>
      <port name="irradianceRoughness" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Scattering Globals"/>
          <entry key="label" value="Irradiance Roughness"/>
        </metadata>
      </port>
      <port name="refractionGain" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Glass"/>
          <entry key="label" value="Refraction Gain"/>
        </metadata>
      </port>
      <port name="reflectionGain" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Glass"/>
          <entry key="label" value="Reflection Gain"/>
        </metadata>
      </port>
      <port name="refractionColor" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="page" value="Glass"/>
          <entry key="label" value="Refraction Color"/>
        </metadata>
      </port>
      <port name="glassRoughness" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Glass"/>
          <entry key="label" value="Roughness"/>
        </metadata>
      </port>
      <port name="glassAnisotropy" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Glass.Advanced"/>
          <entry key="label" value="Anisotropy"/>
        </metadata>
      </port>
      <port name="glassAnisotropyDirection" type="in">
        <tags>
          <tag name="vector"/>
        </tags>
        <metadata>
          <entry key="page" value="Glass.Advanced"/>
          <entry key="label" value="Shading Tangent"/>
        </metadata>
      </port>
      <port name="glassBumpNormal" type="in">
        <tags>
          <tag name="normal"/>
        </tags>
        <metadata>
          <entry key="page" value="Glass.Advanced"/>
          <entry key="label" value="Bump"/>
        </metadata>
      </port>
      <port name="glassIor" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Glass.Advanced"/>
          <entry key="label" value="Refractive Index"/>
        </metadata>
      </port>
      <port name="mwIor" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Glass.Advanced"/>
          <entry key="label" value="Manifold Walk IOR"/>
        </metadata>
      </port>
      <port name="ssAlbedo" type="in">
        <metadata>
          <entry key="page" value="Glass.Interior"/>
          <entry key="label" value="Single Scatter Albedo"/>
        </metadata>
      </port>
      <port name="extinction" type="in">
        <metadata>
          <entry key="page" value="Glass.Interior"/>
          <entry key="label" value="Extinction"/>
        </metadata>
      </port>
      <port name="glowGain" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Glow"/>
          <entry key="label" value="Gain"/>
        </metadata>
      </port>
      <port name="glowColor" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="page" value="Glow"/>
          <entry key="label" value="Color"/>
        </metadata>
      </port>
      <port name="bumpNormal" type="in">
        <tags>
          <tag name="normal"/>
        </tags>
        <metadata>
          <entry key="page" value="Globals"/>
          <entry key="label" value="Bump"/>
        </metadata>
      </port>
      <port name="shadowColor" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="page" value="Globals"/>
          <entry key="label" value="Shadow Color"/>
        </metadata>
      </port>
      <port name="presence" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="page" value="Globals"/>
          <entry key="label" value="Presence"/>
        </metadata>
      </port>
      <port name="userColor" type="in">
        <tags>
          <tag name="color"/>
        </tags>
        <metadata>
          <entry key="page" value="Globals"/>
          <entry key="label" value="User Color"/>
        </metadata>
      </port>
      <port name="utilityPattern" type="in">
        <tags>
          <tag name="int"/>
        </tags>
        <metadata>
          <entry key="label" value="Utility Pattern"/>
        </metadata>
      </port>
      <port name="out" type="out">
        <tags>
          <tag name="bxdf"/>
        </tags>
      </port>
      <group_parameter name="{nodeName}_PSN">
        <string_parameter name="name" value="{nodeName}_PSN"/>
        <string_parameter name="nodeType" value="PxrSurface"/>
        <string_parameter name="__lastValue" value="bnj5wn4igo4ffbcaxtbhjfwtcm2xs55mnnd435bgzmes4bhqmggqFalse"/>
        <string_parameter name="__showHiddenParams" value="False"/>
        <group_parameter name="parameters">
          <group_parameter name="inputMaterial">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="diffuseGain">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="1"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="diffuseColor">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0.18"/>
              <number_parameter name="i1" value="0.18"/>
              <number_parameter name="i2" value="0.18"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="diffuseRoughness">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="diffuseExponent">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="1"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="diffuseBumpNormal">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="diffuseDoubleSided">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="diffuseBackUseDiffuseColor">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="1"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="diffuseBackColor">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0.18"/>
              <number_parameter name="i1" value="0.18"/>
              <number_parameter name="i2" value="0.18"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="diffuseTransmitGain">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="diffuseTransmitColor">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0.18"/>
              <number_parameter name="i1" value="0.18"/>
              <number_parameter name="i2" value="0.18"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="specularFresnelMode">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="specularFaceColor">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="specularEdgeColor">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="specularFresnelShape">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="5"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="specularIor">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="1.5"/>
              <number_parameter name="i1" value="1.5"/>
              <number_parameter name="i2" value="1.5"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="specularExtinctionCoeff">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="specularRoughness">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0.2"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="specularModelType">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="specularAnisotropy">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="specularAnisotropyDirection">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="specularBumpNormal">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="specularDoubleSided">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="roughSpecularFresnelMode">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="roughSpecularFaceColor">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="roughSpecularEdgeColor">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="roughSpecularFresnelShape">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="5"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="roughSpecularIor">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="1.5"/>
              <number_parameter name="i1" value="1.5"/>
              <number_parameter name="i2" value="1.5"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="roughSpecularExtinctionCoeff">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="roughSpecularRoughness">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0.6"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="roughSpecularModelType">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="roughSpecularAnisotropy">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="roughSpecularAnisotropyDirection">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="roughSpecularBumpNormal">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="roughSpecularDoubleSided">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="clearcoatFresnelMode">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="clearcoatFaceColor">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="clearcoatEdgeColor">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="clearcoatFresnelShape">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="5"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="clearcoatIor">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="1.5"/>
              <number_parameter name="i1" value="1.5"/>
              <number_parameter name="i2" value="1.5"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="clearcoatExtinctionCoeff">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="clearcoatThickness">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="clearcoatAbsorptionTint">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="clearcoatRoughness">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="clearcoatModelType">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="clearcoatAnisotropy">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="clearcoatAnisotropyDirection">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="clearcoatBumpNormal">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="clearcoatDoubleSided">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="specularEnergyCompensation">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="clearcoatEnergyCompensation">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="iridescenceFaceGain">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="iridescenceEdgeGain">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="iridescenceFresnelShape">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="5"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="iridescenceMode">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="iridescencePrimaryColor">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="1"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="iridescenceSecondaryColor">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="1"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="iridescenceRoughness">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0.2"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="iridescenceAnisotropy">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="iridescenceAnisotropyDirection">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="iridescenceBumpNormal">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="iridescenceCurve">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="1"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="iridescenceScale">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="1"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="iridescenceFlip">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="iridescenceThickness">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="800"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="iridescenceDoubleSided">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="fuzzGain">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="fuzzColor">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="1"/>
              <number_parameter name="i1" value="1"/>
              <number_parameter name="i2" value="1"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="fuzzConeAngle">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="8"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="fuzzBumpNormal">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="fuzzDoubleSided">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="subsurfaceType">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="subsurfaceGain">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="subsurfaceColor">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0.83"/>
              <number_parameter name="i1" value="0.791"/>
              <number_parameter name="i2" value="0.753"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="subsurfaceDmfp">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="10"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="subsurfaceDmfpColor">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0.851"/>
              <number_parameter name="i1" value="0.5570000000000001"/>
              <number_parameter name="i2" value="0.395"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="shortSubsurfaceGain">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="shortSubsurfaceColor">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0.9"/>
              <number_parameter name="i1" value="0.9"/>
              <number_parameter name="i2" value="0.9"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="shortSubsurfaceDmfp">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="5"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="longSubsurfaceGain">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="longSubsurfaceColor">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0.8"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="longSubsurfaceDmfp">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="20"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="subsurfaceDirectionality">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="subsurfaceBleed">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="subsurfaceDiffuseBlend">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="subsurfaceResolveSelfIntersections">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="subsurfaceIor">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="1.4"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="subsurfacePostTint">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="1"/>
              <number_parameter name="i1" value="1"/>
              <number_parameter name="i2" value="1"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="subsurfaceDiffuseSwitch">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="1"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="subsurfaceDoubleSided">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="subsurfaceTransmitGain">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="considerBackside">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="1"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="continuationRayMode">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="maxContinuationHits">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="2"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="followTopology">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="subsurfaceSubset">
            <number_parameter name="enable" value="0"/>
            <string_parameter name="value" value=""/>
            <string_parameter name="type" value="StringAttr"/>
          </group_parameter>
          <group_parameter name="singlescatterGain">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="singlescatterColor">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0.83"/>
              <number_parameter name="i1" value="0.791"/>
              <number_parameter name="i2" value="0.753"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="singlescatterMfp">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="10"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="singlescatterMfpColor">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0.851"/>
              <number_parameter name="i1" value="0.5570000000000001"/>
              <number_parameter name="i2" value="0.395"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="singlescatterDirectionality">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="singlescatterIor">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="1.3"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="singlescatterBlur">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="singlescatterDirectGain">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="singlescatterDirectGainTint">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="1"/>
              <number_parameter name="i1" value="1"/>
              <number_parameter name="i2" value="1"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="singlescatterDoubleSided">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="singlescatterConsiderBackside">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="1"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="singlescatterContinuationRayMode">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="singlescatterMaxContinuationHits">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="2"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="singlescatterDirectGainMode">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="singlescatterSubset">
            <number_parameter name="enable" value="0"/>
            <string_parameter name="value" value=""/>
            <string_parameter name="type" value="StringAttr"/>
          </group_parameter>
          <group_parameter name="irradianceTint">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="1"/>
              <number_parameter name="i1" value="1"/>
              <number_parameter name="i2" value="1"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="irradianceRoughness">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="unitLength">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0.1"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="refractionGain">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="reflectionGain">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="refractionColor">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="1"/>
              <number_parameter name="i1" value="1"/>
              <number_parameter name="i2" value="1"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="glassRoughness">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0.1"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="glassAnisotropy">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="glassAnisotropyDirection">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="glassBumpNormal">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="glassIor">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="1.5"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="mwWalkable">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="mwIor">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="-1"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="thinGlass">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="ignoreFresnel">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="ignoreAccumOpacity">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="blocksVolumes">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="ssAlbedo">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="extinction">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="g">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="multiScatter">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="enableOverlappingVolumes">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="glowGain">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="glowColor">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="1"/>
              <number_parameter name="i1" value="1"/>
              <number_parameter name="i2" value="1"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="bumpNormal">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="shadowColor">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="shadowMode">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="presence">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="1"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="presenceCached">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="1"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="mwStartable">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="roughnessMollificationClamp">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="32"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="userColor">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="utilityPattern">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="isDynamicArray" value="1"/>
            <numberarray_parameter name="value" size="1" tupleSize="1">
              <number_parameter name="i0" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="__unused"/>
        </group_parameter>
        <group_parameter name="publicInterface">
          <string_parameter name="namePrefix" value=""/>
          <string_parameter name="pagePrefix" value=""/>
          <string_parameter name="nameRegExFind" value=""/>
          <string_parameter name="nameRegExReplace" value=""/>
          <string_parameter name="pageRegExFind" value=""/>
          <string_parameter name="pageRegExReplace" value=""/>
        </group_parameter>
        <string_parameter name="forceRefresh" value=""/>
      </group_parameter>
    </node>
  </node>
</katana>
'''
    
    print(xmlTree)

psnProcedural('1234555555555')
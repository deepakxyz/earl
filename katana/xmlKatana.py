from Katana import KatanaFile, NodegraphAPI 
xmlTree ='''<katana release="3.0v1" version="3.0.1.000002">
  <node name="__SAVE_exportedNodes" type="Group">
    <node baseType="PrmanShadingNode" edited="true" name="displace" selected="true" type="PrmanShadingNode" viewed="true" x="211.000002" y="301.999995">
      <port name="dispAmount" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="label" value="Gain"/>
        </metadata>
      </port>
      <port name="dispScalar" source="transformDisplace.resultF" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="label" value="Scalar Displacement"/>
        </metadata>
      </port>
      <port name="dispVector" type="in">
        <tags>
          <tag name="vector"/>
        </tags>
        <metadata>
          <entry key="label" value="Vector Displacement"/>
        </metadata>
      </port>
      <port name="modelDispVector" type="in">
        <tags>
          <tag name="vector"/>
        </tags>
        <metadata>
          <entry key="label" value="Model Displacement"/>
        </metadata>
      </port>
      <port name="out" type="out">
        <tags>
          <tag name="displacement"/>
        </tags>
      </port>
      <group_parameter name="displace">
        <string_parameter name="name" value="displace"/>
        <string_parameter name="nodeType" value="PxrDisplace"/>
        <string_parameter name="__lastValue" value="gawyiry6nxrydvwasolt7sqdhimkhgcbmnnt2qp2lvxz3yisfhniFalse"/>
        <string_parameter name="__showHiddenParams" value="False"/>
        <group_parameter name="parameters">
          <group_parameter name="enabled">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="1"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="dispAmount">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="1"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="dispScalar">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="dispVector">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="modelDispVector">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
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
    <node baseType="PrmanShadingNode" name="transformDisplace" selected="true" type="PrmanShadingNode" x="200" y="350">
      <port name="dispScalar" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="label" value="Scalar Displacement"/>
        </metadata>
      </port>
      <port name="dispVector" type="in">
        <tags>
          <tag name="color or vector"/>
        </tags>
        <metadata>
          <entry key="label" value="Vector Displacement"/>
        </metadata>
      </port>
      <port name="dispHeight" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="label" value="Displacement Height"/>
        </metadata>
      </port>
      <port name="dispDepth" type="in">
        <tags>
          <tag name="float"/>
        </tags>
        <metadata>
          <entry key="label" value="Displacement Depth"/>
        </metadata>
      </port>
      <port name="dispDirection" type="in">
        <metadata>
          <entry key="page" value="Advanced"/>
          <entry key="label" value="Displacement Direction"/>
        </metadata>
      </port>
      <port name="resultXYZ" type="out">
        <tags>
          <tag name="vector"/>
        </tags>
      </port>
      <port name="resultF" type="out">
        <tags>
          <tag name="float"/>
        </tags>
      </port>
      <group_parameter name="transformDisplace">
        <string_parameter name="name" value="transformDisplace"/>
        <string_parameter name="nodeType" value="PxrDispTransform"/>
        <string_parameter name="__lastValue" value="uxukk3tnxqgnb3h2rplxcdm7w4tilrppls7qi37ddk25jgfjairuFalse"/>
        <string_parameter name="__showHiddenParams" value="False"/>
        <group_parameter name="parameters">
          <group_parameter name="dispType">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="1"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="dispScalar">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="dispVector">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="vectorSpace">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="3"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="dispHeight">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="1"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="dispDepth">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="1"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="dispRemapMode">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="1"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="dispCenter">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0.5"/>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="dispScaleSpace">
            <number_parameter name="enable" value="0"/>
            <string_parameter name="value" value="object"/>
            <string_parameter name="type" value="StringAttr"/>
          </group_parameter>
          <group_parameter name="useDispDirection">
            <number_parameter name="enable" value="0"/>
            <number_parameter name="value" value="0"/>
            <string_parameter name="type" value="IntAttr"/>
          </group_parameter>
          <group_parameter name="dispDirection">
            <number_parameter name="enable" value="0"/>
            <numberarray_parameter name="value" size="3" tupleSize="3">
              <number_parameter name="i0" value="0"/>
              <number_parameter name="i1" value="0"/>
              <number_parameter name="i2" value="0"/>
            </numberarray_parameter>
            <string_parameter name="type" value="FloatAttr"/>
          </group_parameter>
          <group_parameter name="dispDirectionSpace">
            <number_parameter name="enable" value="0"/>
            <string_parameter name="value" value="object"/>
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
  </node>
</katana> '''

root = NodegraphAPI.GetRootNode()
KatanaFile.Paste( xmlTree, root )


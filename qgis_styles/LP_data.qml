<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis readOnly="0" styleCategories="LayerConfiguration|Symbology|Symbology3D|Labeling" labelsEnabled="1" version="3.14.1-Pi">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 forceraster="0" symbollevels="0" enableorderby="0" type="singleSymbol">
    <symbols>
      <symbol clip_to_extent="1" name="0" alpha="1" force_rhr="0" type="line">
        <layer locked="0" enabled="1" pass="0" class="GeometryGenerator">
          <prop k="SymbolType" v="Line"/>
          <prop k="geometryModifier" v="difference(&#xd;&#xa;   difference(&#xd;&#xa;      make_line(&#xd;&#xa;         start_point($geometry),&#xd;&#xa;         centroid(&#xd;&#xa;            offset_curve(&#xd;&#xa;               $geometry, &#xd;&#xa;               length($geometry)/5.0&#xd;&#xa;            )&#xd;&#xa;         ),&#xd;&#xa;     end_point($geometry)&#xd;&#xa;      ),&#xd;&#xa;      buffer(start_point($geometry), 10)&#xd;&#xa;   ),&#xd;&#xa;   buffer(end_point( $geometry), 10)&#xd;&#xa;)"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" name="@0@0" alpha="1" force_rhr="0" type="line">
            <layer locked="0" enabled="1" pass="0" class="ArrowLine">
              <prop k="arrow_start_width" v="1"/>
              <prop k="arrow_start_width_unit" v="MM"/>
              <prop k="arrow_start_width_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="arrow_type" v="0"/>
              <prop k="arrow_width" v="1"/>
              <prop k="arrow_width_unit" v="MM"/>
              <prop k="arrow_width_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="head_length" v="4"/>
              <prop k="head_length_unit" v="MM"/>
              <prop k="head_length_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="head_thickness" v="2"/>
              <prop k="head_thickness_unit" v="MM"/>
              <prop k="head_thickness_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="head_type" v="0"/>
              <prop k="is_curved" v="1"/>
              <prop k="is_repeated" v="0"/>
              <prop k="offset" v="0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="offset_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="ring_filter" v="0"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" type="QString" value=""/>
                  <Option name="properties"/>
                  <Option name="type" type="QString" value="collection"/>
                </Option>
              </data_defined_properties>
              <symbol clip_to_extent="1" name="@@0@0@0" alpha="1" force_rhr="0" type="fill">
                <layer locked="0" enabled="1" pass="0" class="SimpleFill">
                  <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="color" v="255,0,0,89"/>
                  <prop k="joinstyle" v="bevel"/>
                  <prop k="offset" v="0,0"/>
                  <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
                  <prop k="offset_unit" v="MM"/>
                  <prop k="outline_color" v="35,35,35,255"/>
                  <prop k="outline_style" v="no"/>
                  <prop k="outline_width" v="0.26"/>
                  <prop k="outline_width_unit" v="MM"/>
                  <prop k="style" v="solid"/>
                  <data_defined_properties>
                    <Option type="Map">
                      <Option name="name" type="QString" value=""/>
                      <Option name="properties"/>
                      <Option name="type" type="QString" value="collection"/>
                    </Option>
                  </data_defined_properties>
                </layer>
              </symbol>
            </layer>
          </symbol>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <labeling type="simple">
    <settings calloutType="simple">
      <text-style isExpression="0" previewBkgrdColor="255,255,255,255" fontSizeMapUnitScale="3x:0,0,0,0,0,0" namedStyle="Regular" blendMode="0" textOrientation="horizontal" fontWordSpacing="0" textColor="255,0,0,255" useSubstitutions="0" fontLetterSpacing="0" multilineHeight="1" fontWeight="50" fontUnderline="0" fontSize="8" fontCapitals="0" fontItalic="0" fieldName="LP_data" fontFamily="Arial" fontSizeUnit="Point" allowHtml="0" textOpacity="1" fontStrikeout="0" fontKerning="1">
        <text-buffer bufferBlendMode="0" bufferSizeUnits="MM" bufferOpacity="1" bufferDraw="1" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferSize="1" bufferJoinStyle="128" bufferNoFill="1" bufferColor="255,255,255,255"/>
        <text-mask maskEnabled="0" maskSizeUnits="MM" maskType="0" maskSize="1.5" maskJoinStyle="128" maskSizeMapUnitScale="3x:0,0,0,0,0,0" maskedSymbolLayers="" maskOpacity="1"/>
        <background shapeRadiiUnit="MM" shapeSizeType="0" shapeRotation="0" shapeRadiiY="0" shapeOffsetY="0" shapeBlendMode="0" shapeSizeX="0" shapeJoinStyle="64" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthUnit="MM" shapeOffsetX="0" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeOpacity="1" shapeSVGFile="" shapeDraw="0" shapeBorderColor="128,128,128,255" shapeFillColor="255,255,255,255" shapeSizeUnit="MM" shapeOffsetUnit="MM" shapeRotationType="0" shapeRadiiX="0" shapeBorderWidth="0" shapeSizeY="0" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeType="0">
          <symbol clip_to_extent="1" name="markerSymbol" alpha="1" force_rhr="0" type="marker">
            <layer locked="0" enabled="1" pass="0" class="SimpleMarker">
              <prop k="angle" v="0"/>
              <prop k="color" v="231,113,72,255"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="circle"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_color" v="35,35,35,255"/>
              <prop k="outline_style" v="solid"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="scale_method" v="diameter"/>
              <prop k="size" v="2"/>
              <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" type="QString" value=""/>
                  <Option name="properties"/>
                  <Option name="type" type="QString" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </background>
        <shadow shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowOffsetUnit="MM" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowBlendMode="6" shadowDraw="0" shadowUnder="0" shadowOffsetAngle="135" shadowRadius="1.5" shadowOpacity="0.7" shadowColor="0,0,0,255" shadowRadiusAlphaOnly="0" shadowOffsetGlobal="1" shadowRadiusUnit="MM" shadowOffsetDist="1" shadowScale="100"/>
        <dd_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties"/>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </dd_properties>
        <substitutions/>
      </text-style>
      <text-format autoWrapLength="0" reverseDirectionSymbol="0" useMaxLineLengthForAutoWrap="1" addDirectionSymbol="0" decimals="3" multilineAlign="0" formatNumbers="0" plussign="0" placeDirectionSymbol="0" rightDirectionSymbol=">" wrapChar="" leftDirectionSymbol="&lt;"/>
      <placement polygonPlacementFlags="2" maxCurvedCharAngleOut="-30" repeatDistance="0" yOffset="0" offsetUnits="MM" centroidWhole="0" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" preserveRotation="1" geometryGenerator="difference(&#xd;&#xa;   difference(&#xd;&#xa;      make_line(&#xd;&#xa;         start_point($geometry),&#xd;&#xa;         centroid(&#xd;&#xa;            offset_curve(&#xd;&#xa;               $geometry, &#xd;&#xa;               length($geometry)/5.0&#xd;&#xa;            )&#xd;&#xa;         ),&#xd;&#xa;     end_point($geometry)&#xd;&#xa;      ),&#xd;&#xa;      buffer(start_point($geometry), 10)&#xd;&#xa;   ),&#xd;&#xa;   buffer(end_point( $geometry), 10)&#xd;&#xa;)" layerType="LineGeometry" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" fitInPolygonOnly="0" geometryGeneratorType="LineGeometry" distMapUnitScale="3x:0,0,0,0,0,0" priority="5" overrunDistanceUnit="MM" maxCurvedCharAngleIn="30" dist="0" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" repeatDistanceUnits="MM" placement="3" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" placementFlags="9" offsetType="0" quadOffset="4" centroidInside="0" rotationAngle="0" overrunDistance="0" xOffset="0" distUnits="MM" geometryGeneratorEnabled="1"/>
      <rendering obstacleFactor="1" zIndex="0" obstacleType="1" displayAll="0" scaleMax="0" minFeatureSize="0" fontLimitPixelSize="0" limitNumLabels="0" drawLabels="1" mergeLines="0" upsidedownLabels="0" obstacle="1" maxNumLabels="2000" scaleMin="0" fontMinPixelSize="3" scaleVisibility="0" fontMaxPixelSize="10000" labelPerPart="0"/>
      <dd_properties>
        <Option type="Map">
          <Option name="name" type="QString" value=""/>
          <Option name="properties" type="Map">
            <Option name="Hali" type="Map">
              <Option name="active" type="bool" value="false"/>
              <Option name="type" type="int" value="1"/>
              <Option name="val" type="QString" value=""/>
            </Option>
            <Option name="PositionX" type="Map">
              <Option name="active" type="bool" value="false"/>
              <Option name="type" type="int" value="1"/>
              <Option name="val" type="QString" value=""/>
            </Option>
            <Option name="PositionY" type="Map">
              <Option name="active" type="bool" value="false"/>
              <Option name="type" type="int" value="1"/>
              <Option name="val" type="QString" value=""/>
            </Option>
          </Option>
          <Option name="type" type="QString" value="collection"/>
        </Option>
      </dd_properties>
      <callout type="simple">
        <Option type="Map">
          <Option name="anchorPoint" type="QString" value="pole_of_inaccessibility"/>
          <Option name="ddProperties" type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties"/>
            <Option name="type" type="QString" value="collection"/>
          </Option>
          <Option name="drawToAllParts" type="bool" value="false"/>
          <Option name="enabled" type="QString" value="0"/>
          <Option name="labelAnchorPoint" type="QString" value="point_on_exterior"/>
          <Option name="lineSymbol" type="QString" value="&lt;symbol clip_to_extent=&quot;1&quot; name=&quot;symbol&quot; alpha=&quot;1&quot; force_rhr=&quot;0&quot; type=&quot;line&quot;>&lt;layer locked=&quot;0&quot; enabled=&quot;1&quot; pass=&quot;0&quot; class=&quot;SimpleLine&quot;>&lt;prop k=&quot;capstyle&quot; v=&quot;square&quot;/>&lt;prop k=&quot;customdash&quot; v=&quot;5;2&quot;/>&lt;prop k=&quot;customdash_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;customdash_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;draw_inside_polygon&quot; v=&quot;0&quot;/>&lt;prop k=&quot;joinstyle&quot; v=&quot;bevel&quot;/>&lt;prop k=&quot;line_color&quot; v=&quot;60,60,60,255&quot;/>&lt;prop k=&quot;line_style&quot; v=&quot;solid&quot;/>&lt;prop k=&quot;line_width&quot; v=&quot;0.3&quot;/>&lt;prop k=&quot;line_width_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;offset&quot; v=&quot;0&quot;/>&lt;prop k=&quot;offset_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;prop k=&quot;offset_unit&quot; v=&quot;MM&quot;/>&lt;prop k=&quot;ring_filter&quot; v=&quot;0&quot;/>&lt;prop k=&quot;use_custom_dash&quot; v=&quot;0&quot;/>&lt;prop k=&quot;width_map_unit_scale&quot; v=&quot;3x:0,0,0,0,0,0&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option name=&quot;name&quot; type=&quot;QString&quot; value=&quot;&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option name=&quot;type&quot; type=&quot;QString&quot; value=&quot;collection&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>"/>
          <Option name="minLength" type="double" value="0"/>
          <Option name="minLengthMapUnitScale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="minLengthUnit" type="QString" value="MM"/>
          <Option name="offsetFromAnchor" type="double" value="0"/>
          <Option name="offsetFromAnchorMapUnitScale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="offsetFromAnchorUnit" type="QString" value="MM"/>
          <Option name="offsetFromLabel" type="double" value="0"/>
          <Option name="offsetFromLabelMapUnitScale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="offsetFromLabelUnit" type="QString" value="MM"/>
        </Option>
      </callout>
    </settings>
  </labeling>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <previewExpression>"fid"</previewExpression>
  <layerGeometryType>1</layerGeometryType>
</qgis>

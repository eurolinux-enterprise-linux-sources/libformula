Name: libformula
Version: 1.1.3
Release: 10%{?dist}
Summary: Formula Parser
License: LGPLv2
Group: System Environment/Libraries
#Original source: http://downloads.sourceforge.net/jfreereport/%{name}-%{version}.zip
#unzip, find . -name "*.jar" -exec rm {} \;
#to simplify the licensing
Source: %{name}-%{version}-jarsdeleted.zip
URL: http://reporting.pentaho.org/
BuildRequires: ant, ant-contrib, java-devel, jpackage-utils, libbase >= 1.1.3
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: java, jpackage-utils, apache-commons-logging, libbase >= 1.1.3
BuildArch: noarch
Patch0: libformula-1.1.2.build.patch

%description
LibFormula provides Excel-Style-Expressions. The implementation provided
here is very generic and can be used in any application that needs to
compute formulas.

%package javadoc
Summary: Javadoc for %{name}
Group: Development/Documentation
Requires: %{name} = %{version}-%{release}
Requires: jpackage-utils

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c
%patch0 -p1 -b .build
find . -name "*.jar" -exec rm -f {} \;
mkdir -p lib
build-jar-repository -s -p lib commons-logging-api libbase
cd lib
ln -s %{_javadir}/ant ant-contrib

%build
ant jar javadoc

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p ./dist/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
pushd $RPM_BUILD_ROOT%{_javadir}
ln -s %{name}-%{version}.jar %{name}.jar
popd

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp bin/javadoc/docs/api $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,0755)
%doc licence-LGPL.txt README.txt ChangeLog.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.1.3-10
- Mass rebuild 2013-12-27

* Fri Dec 06 2013 Caolán McNamara <caolanm@redhat.com> - 1.1.3-9
- Resolves: rhbz#1038178 ant-nodeps dropped

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 03 2012 Caolán McNamara <caolanm@redhat.com> - 1.1.3-7
- repack source to remove bundled multi-license .jars

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 03 2012 Caolán McNamara <caolanm@redhat.com> 1.1.3-5
- Resolves: rhbz#818494 adapt for jakarta->apache

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 28 2011 Caolán McNamara <caolanm@redhat.com> 1.1.3-3
- Related: rhbz#749103 drop gcj aot

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 03 2009 Caolan McNamara <caolanm@redhat.com> 1.1.3-1
- latest version

* Tue Nov 17 2009 Caolan McNamara <caolanm@redhat.com> 1.1.2-1
- latest version

* Fri Jul 24 2009 Caolan McNamara <caolanm@redhat.com> 0.2.0-3.OOo31
- make javadoc no-arch when building as arch-dependant aot

* Mon Mar 16 2009 Caolan McNamara <caolanm@redhat.com> 0.2.0-2.OOo31
- post-release tuned for OpenOffice.org report-designer

* Mon Mar 09 2009 Caolan McNamara <caolanm@redhat.com> 0.2.0-1
- latest version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed May 07 2008 Caolan McNamara <caolanm@redhat.com> 0.1.18-1
- initial fedora import

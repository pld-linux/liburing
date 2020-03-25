Summary:	Linux-native io_uring I/O access library
Name:		liburing
Version:	0.5
Release:	1
License:	LGPLv2+ or MIT
Group:		Libraries
Source0:	https://brick.kernel.dk/snaps/%{name}-%{version}.tar.gz
# Source0-md5:	98d9ed88aa260cc0515410f344d57319
URL:		https://git.kernel.dk/cgit/liburing/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides native async IO for the Linux kernel, in a fast and efficient
manner, for both buffered and O_DIRECT.

%package devel
Summary:	Header files and develpment documentation for liburing
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Development files for Linux-native io_uring I/O access library.

%package static
Summary:	Static liburing library
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
This package provides header files to include and libraries to link
with for the Linux-native io_uring.

%prep
%setup -q

%build
./configure \
	--prefix=%{_prefix} \
	--libdir=/%{_libdir} \
	--libdevdir=/%{_libdir} \
	--mandir=%{_mandir} \
	--includedir=%{_includedir}
 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{makeinstall} \
	libdevdir=$RPM_BUILD_ROOT/%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/liburing.so.*.*
%attr(755,root,root) %ghost %{_libdir}/liburing.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liburing.so
%{_includedir}/liburing
%{_includedir}/liburing.h
%{_pkgconfigdir}/liburing.pc
%{_mandir}/man2/io_uring_*.2*

%files static
%defattr(644,root,root,755)
%{_libdir}/liburing.a
